import { useMemo, useState } from "react";
import type { Answers, Question } from "../types";

interface Props {
  questions: Question[];
  languageName: string;
  onSubmit: (answers: Answers) => void;
  onBack: () => void;
  busy: boolean;
}

export default function Questionnaire({
  questions,
  languageName,
  onSubmit,
  onBack,
  busy,
}: Props) {
  const [answers, setAnswers] = useState<Answers>({});

  const toggle = (q: Question, optionId: string) => {
    setAnswers((prev) => {
      const current = prev[q.id] ?? [];
      let next: string[];
      if (q.multi) {
        next = current.includes(optionId)
          ? current.filter((x) => x !== optionId)
          : [...current, optionId];
      } else {
        next = current.includes(optionId) ? [] : [optionId];
      }
      return next.length ? { ...prev, [q.id]: next } : dropKey(prev, q.id);
    });
  };

  const answeredCount = useMemo(
    () => questions.filter((q) => (answers[q.id] ?? []).length > 0).length,
    [answers, questions]
  );

  return (
    <div className="card">
      <button className="link" onClick={onBack}>
        ← change language
      </button>
      <h2>Tell us about yourself</h2>
      <p className="muted">
        Your answers shape which words matter for <strong>your</strong>{" "}
        {languageName}. Skip anything that doesn't apply — the more you answer,
        the more tailored the list.
      </p>

      {questions.map((q) => (
        <fieldset key={q.id} className="question">
          <legend>{q.prompt}</legend>
          {q.help && <p className="help">{q.help}</p>}
          <div className="options">
            {q.options.map((o) => {
              const selected = (answers[q.id] ?? []).includes(o.id);
              return (
                <button
                  type="button"
                  key={o.id}
                  className={`chip ${selected ? "chip-on" : ""}`}
                  aria-pressed={selected}
                  onClick={() => toggle(q, o.id)}
                >
                  {o.label}
                </button>
              );
            })}
          </div>
        </fieldset>
      ))}

      <div className="actions">
        <span className="muted">
          {answeredCount} / {questions.length} answered
        </span>
        <button
          className="primary"
          disabled={busy}
          onClick={() => onSubmit(answers)}
        >
          {busy ? "Building your list…" : "Build my 1000 words"}
        </button>
      </div>
    </div>
  );
}

function dropKey<T extends object>(obj: T, key: string): T {
  const copy = { ...obj } as Record<string, unknown>;
  delete copy[key];
  return copy as T;
}
