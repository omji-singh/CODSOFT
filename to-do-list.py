import tkinter as tk
from tkinter import ttk, messagebox
import json, pathlib, datetime as dt

db_path = pathlib.Path.home() / ".todo_gui.json"

def load():
    if db_path.exists():
        return json.loads(db_path.read_text())
    return []

def save(tasks):
    db_path.write_text(json.dumps(tasks, indent=2))

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To‑Do List")
        self.resizable(False, False)
        self.tasks = load()
        self.build_ui()
        self.refresh()

    def build_ui(self):
        frm = ttk.Frame(self, padding=10)
        frm.grid()

        ttk.Label(frm, text="Task:").grid(row=0, column=0, sticky="e")
        self.entry_task = ttk.Entry(frm, width=30)
        self.entry_task.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(frm, text="Due (YYYY-MM-DD):").grid(row=1, column=0, sticky="e")
        self.entry_due = ttk.Entry(frm, width=15)
        self.entry_due.grid(row=1, column=1, sticky="w", pady=2)

        ttk.Label(frm, text="Priority:").grid(row=2, column=0, sticky="e")
        self.combo_prio = ttk.Combobox(frm, values=[1, 2, 3], width=5, state="readonly")
        self.combo_prio.current(2)  
        self.combo_prio.grid(row=2, column=1, sticky="w", pady=2)

        ttk.Button(frm, text="Add", command=self.add_task).grid(row=3, column=1, sticky="e", pady=4)

        self.tree = ttk.Treeview(
            frm,
            columns=("task", "prio", "due"),
            show="headings",
            height=10
        )
        self.tree.heading("task", text="Task")
        self.tree.heading("prio", text="Priority")
        self.tree.heading("due", text="Due")

        self.tree.column("task", width=200)
        self.tree.column("prio", width=60, anchor="center")
        self.tree.column("due", width=100, anchor="center")

        self.tree.grid(row=4, column=0, columnspan=2, pady=8)

        ttk.Button(frm, text="Mark Done", command=self.mark_done).grid(row=5, column=0, sticky="w")
        ttk.Button(frm, text="Delete", command=self.delete).grid(row=5, column=1, sticky="e")

    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for t in sorted(self.tasks, key=lambda x: (x["done"], x["priority"], x["due"] or "")):
            tag = "done" if t["done"] else ""
            self.tree.insert(
                "", "end",
                iid=t["id"],
                values=(t["text"], t["priority"], t["due"] or ""),
                tags=(tag,)
            )
        self.tree.tag_configure("done", foreground="grey")

    def add_task(self):
        text = self.entry_task.get().strip()
        due_raw = self.entry_due.get().strip()
        prio = int(self.combo_prio.get())

        due = None
        if due_raw:
            try:
                due = dt.date.fromisoformat(due_raw).isoformat()
            except ValueError:
                messagebox.showerror("Invalid Date", "Please enter due date as YYYY-MM-DD.")
                return

        if not text:
            messagebox.showerror("Empty Task", "Please enter a task description.")
            return

        new_id = self.tasks[-1]["id"] + 1 if self.tasks else 1
        self.tasks.append({
            "id": new_id,
            "text": text,
            "due": due,
            "priority": prio,
            "done": False
        })

        save(self.tasks)
        self.entry_task.delete(0, tk.END)
        self.entry_due.delete(0, tk.END)
        self.combo_prio.current(2) 
        self.refresh()

    def mark_done(self):
        sel = self.tree.selection()
        if sel:
            tid = int(sel[0])
            for t in self.tasks:
                if t["id"] == tid:
                    t["done"] = True
                    break
            save(self.tasks)
            self.refresh()

    def delete(self):
        sel = self.tree.selection()
        if sel and messagebox.askyesno("Delete", "Delete task?"):
            tid = int(sel[0])
            self.tasks = [t for t in self.tasks if t["id"] != tid]
            save(self.tasks)
            self.refresh()

if __name__ == "__main__":
    App().mainloop()
