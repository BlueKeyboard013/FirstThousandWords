import { useEffect, useMemo, useState } from "react";
import { downloadCsv } from "../api";
import type { Answers, WordListResponse } from "../types";

interface Props {
  data: WordListResponse;
  answers: Answers;
  onRestart: () => void;
}

type Tab = "core" | "mandatory";

export default function Results({ data, answers, onRestart }: Props) {
  const [tab, setTab] = useState<Tab>("core");
  const [query, setQuery] = useState("");
  const [topic, setTopic] = useState<string>("all");
  const [known, setKnown] = useKnownWords(data.language);

  const filteredCore = useMemo(() => {
    const q = query.trim().toLowerCase();
    return data.core.filter((e) => {
      if (topic !== "all" && !e.topics.includes(topic)) return false;
      if (!q) return true;
      return (
        e.word.toLowerCase().includes(q) || e.gloss.toLowerCase().includes(q)
      );
    });
  }, [data.core, query, topic]);

  const filteredMandatory = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return data.mandatory;
    return data.mandatory.filter(
      (e) =>
        e.word.toLowerCase().includes(q) || e.gloss.toLowerCase().includes(q)
    );
  }, [data.mandatory, query]);

  const knownInCore = data.core.filter((e) => known.has(e.word)).length;

  return (
    <div className="card">
      <button className="link" onClick={onRestart}>
        ← start over
      </button>
      <h2>Your first words in {data.language_name}</h2>
      <p className="muted">
        {data.core_size} personalised words, plus {data.mandatory.length}{" "}
        must-know glue words. Tick words as you learn them — progress is saved in
        this browser.
      </p>

      {data.focus_topics.length > 0 && (
        <div className="topic-tags">
          <span className="muted" style={{ fontSize: 12 }}>tuned to:</span>
          {data.focus_topics.map((t) => (
            <span key={t.id} className="tag">
              {t.label}
            </span>
          ))}
        </div>
      )}

      <div className="tabs">
        <button
          className={tab === "core" ? "tab tab-on" : "tab"}
          onClick={() => setTab("core")}
        >
          Your 1000 words ({knownInCore}/{data.core.length})
        </button>
        <button
          className={tab === "mandatory" ? "tab tab-on" : "tab"}
          onClick={() => setTab("mandatory")}
        >
          Glue words ({data.mandatory.length})
        </button>
      </div>

      <div className="toolbar">
        <input
          className="search"
          placeholder="search word or meaning…"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        {tab === "core" && (
          <select value={topic} onChange={(e) => setTopic(e.target.value)}>
            <option value="all">all topics</option>
            {data.topics_covered.map((t) => (
              <option key={t.id} value={t.id}>
                {t.label}
              </option>
            ))}
          </select>
        )}
        <button className="ghost" onClick={() => downloadCsv(data.language, answers)}>
          Download CSV
        </button>
      </div>

      {tab === "core" ? (
        <ol className="wordlist">
          {filteredCore.map((e) => (
            <li key={e.word} className={known.has(e.word) ? "row done" : "row"}>
              <label>
                <input
                  type="checkbox"
                  checked={known.has(e.word)}
                  onChange={() => setKnown(e.word)}
                />
                <span className="rank">{e.rank}</span>
                <span className="word">{e.word}</span>
                <span className="gloss">{e.gloss || "—"}</span>
              </label>
              <span className="pills">
                {e.topic_labels.map((l) => (
                  <span key={l} className="pill">
                    {l}
                  </span>
                ))}
              </span>
            </li>
          ))}
          {filteredCore.length === 0 && <li className="empty">No matches.</li>}
        </ol>
      ) : (
        <ul className="wordlist">
          {filteredMandatory.map((e) => (
            <li key={e.word} className={known.has(e.word) ? "row done" : "row"}>
              <label>
                <input
                  type="checkbox"
                  checked={known.has(e.word)}
                  onChange={() => setKnown(e.word)}
                />
                <span className="word">{e.word}</span>
                <span className="gloss">{e.gloss}</span>
              </label>
            </li>
          ))}
          {filteredMandatory.length === 0 && <li className="empty">No matches.</li>}
        </ul>
      )}
    </div>
  );
}

function useKnownWords(language: string) {
  const key = `ftw:known:${language}`;
  const [known, setSet] = useState<Set<string>>(() => {
    try {
      const raw = localStorage.getItem(key);
      return new Set<string>(raw ? JSON.parse(raw) : []);
    } catch {
      return new Set<string>();
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem(key, JSON.stringify([...known]));
    } catch {
      /* ignore */
    }
  }, [key, known]);

  const toggle = (word: string) =>
    setSet((prev) => {
      const next = new Set(prev);
      next.has(word) ? next.delete(word) : next.add(word);
      return next;
    });

  return [known, toggle] as const;
}
