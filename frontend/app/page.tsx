"use client";

import { useState } from "react";

export default function Home() {
  const [problem, setProblem] = useState("Résous 2x + 3 = 11");
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState<any>(null);

  const solve = async () => {
    setLoading(true);
    try {
      const res = await fetch("http://localhost:8000/api/solve", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ problem }),
      });

      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error(error);
      setResponse({ error: "Impossible de joindre le backend. Démarre le serveur FastAPI sur le port 8000." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-slate-950 text-white px-6 py-10">
      <div className="mx-auto max-w-4xl">
        <div className="mb-10">
          <p className="text-sm uppercase tracking-[0.2em] text-blue-400">Math AI Assistant</p>
          <h1 className="mt-3 text-4xl font-bold">Résolvez vos problèmes de maths</h1>
        </div>

        <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6 shadow-2xl">
          <label className="mb-2 block text-sm text-slate-300">Votre problème</label>
          <textarea
            value={problem}
            onChange={(e) => setProblem(e.target.value)}
            className="h-28 w-full rounded-xl border border-slate-700 bg-slate-950 p-4 text-lg text-white outline-none ring-0 placeholder:text-slate-500"
            placeholder="Exemple : Résous 2x + 3 = 11"
          />

          <button
            onClick={solve}
            disabled={loading}
            className="mt-5 rounded-xl bg-blue-600 px-5 py-3 font-semibold text-white transition hover:bg-blue-500 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Calcul en cours..." : "Résoudre"}
          </button>
        </div>

        {response && (
          <div className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6">
            {response.error ? (
              <p className="text-red-400">{response.error}</p>
            ) : (
              <>
                <div className="mb-6">
                  <h2 className="text-xl font-semibold mb-2">Résultat</h2>
                  <pre className="overflow-x-auto whitespace-pre-wrap rounded-lg bg-slate-950 p-4 text-sm text-slate-200">
                    {JSON.stringify(response.result, null, 2)}
                  </pre>
                </div>

                <div>
                  <h2 className="text-xl font-semibold mb-2">Explication</h2>
                  <p className="whitespace-pre-wrap text-slate-200">{response.explanation}</p>
                </div>
              </>
            )}
          </div>
        )}

        <div className="mt-8 grid gap-4 md:grid-cols-3">
          <ExampleCard text="Résous 2x + 3 = 11" onClick={() => setProblem("Résous 2x + 3 = 11")} />
          <ExampleCard text="Dérive x^2 + 3x + 1" onClick={() => setProblem("Dérive x^2 + 3x + 1")} />
          <ExampleCard text="Intègre x^2 + 1" onClick={() => setProblem("Intègre x^2 + 1")} />
        </div>
      </div>
    </main>
  );
}

function ExampleCard({ text, onClick }: { text: string; onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      className="rounded-xl border border-slate-700 bg-slate-900 p-4 text-left text-slate-200 transition hover:border-blue-500 hover:bg-slate-800"
    >
      {text}
    </button>
  );
}
