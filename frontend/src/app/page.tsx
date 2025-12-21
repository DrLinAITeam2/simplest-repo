"use client";

import { useState, useEffect } from "react";

enum TaskStatus {
  PENDING = "pending",
  IN_PROGRESS = "in_progress",
  BLOCKED = "blocked",
  COMPLETED = "completed",
  FAILED = "failed",
  CANCELLED = "cancelled",
}

const API_BASE = 'http://localhost:8000';

export default function Home() {
  const [current, setCurrent] = useState<TaskStatus>(TaskStatus.PENDING);
  const [allowed, setAllowed] = useState<Set<TaskStatus>>(new Set());

  useEffect(() => {
    fetch(`${API_BASE}/transitions/${current}`)
      .then(res => res.json())
      .then(data => setAllowed(new Set(data.map((s: string) => s as TaskStatus))))
      .catch(err => console.error('Failed to fetch transitions:', err));
  }, [current]);

  const handleTransition = async (target: TaskStatus) => {
    try {
      const res = await fetch(`${API_BASE}/transition`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ current, target }),
      });
      const data = await res.json();
      if (data.success) {
        setCurrent(data.new_status as TaskStatus);
      } else {
        alert(`Transition failed: ${data.error}`);
      }
    } catch (err) {
      console.error('Transition error:', err);
      alert('Failed to transition');
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-col items-center justify-center py-32 px-16 bg-white dark:bg-black rounded-lg shadow-lg">
        <h1 className="text-3xl font-semibold leading-10 tracking-tight text-black dark:text-zinc-50 mb-8">
          Task Status Transition Demo
        </h1>
        <p className="text-lg text-zinc-600 dark:text-zinc-400 mb-6">
          Current Status: <span className="font-medium text-black dark:text-zinc-50">{current}</span>
        </p>
        <div className="flex flex-wrap gap-4">
          {Object.values(TaskStatus).map((status) => (
            <button
              key={status}
              onClick={() => handleTransition(status)}
              disabled={!allowed.has(status)}
              className={`px-4 py-2 rounded-full font-medium transition-colors ${
                allowed.has(status)
                  ? "bg-blue-500 text-white hover:bg-blue-600"
                  : "bg-gray-300 text-gray-500 cursor-not-allowed"
              }`}
            >
              Transition to {status}
            </button>
          ))}
        </div>
      </main>
    </div>
  );
}
