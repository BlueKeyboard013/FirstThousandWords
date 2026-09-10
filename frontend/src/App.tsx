import { useEffect, useState } from "react";
import { buildWordList, getLanguages, getQuestions } from "./api";
import Questionnaire from "./components/Questionnaire";
import Results from "./components/Results";
import type { Answers, Language, Question, WordListResponse } from "./types";

type Step = "language" | "questions" | "results";

export default function App() {
  const [step, setStep] = useState<Step>("language");
  const [languages, setLanguages] = useState<Language[]>([]);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [language, setLanguage] = useState<Language | null>(null);
  const [answers, setAnswers] = useState<Answers>({});
  const [result, setResult] = useState<WordListResponse | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    Promise.all([getLanguages(), getQuestions()])
      .then(([langs, qs]) => {
        setLanguages(langs);
        setQuestions(qs);
      })
      .catch(() => setError("Could not reach the backend. Is it running on :8000?"));
  }, []);

  const submit = async (a: Answers) => {
    if (!language) return;
    setBusy(true);
    setError(null);
    try {
      const data = await buildWordList(language.code, a);
      setAnswers(a);
      setResult(data);
      setStep("results");
    } catch {
      setError("Something went wrong building your list. Try again.");
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="page">
      <header>
        <h1>First 1000 Words</h1>
        <p className="tagline">
          The words worth learning first — tuned to what you actually talk about.
        </p>
      </header>

      {error && <div className="error">{error}</div>}

      {step === "language" && (
        <div className="card">
          <h2>Which language are you learning?</h2>
          <div className="lang-grid">
            {languages.map((l) => (
              <button
                key={l.code}
                className="lang-btn"
                onClick={() => {
                  setLanguage(l);
                  setStep("questions");
                }}
              >
                {l.name}
              </button>
            ))}
            {languages.length === 0 && !error && <p className="muted">Loading…</p>}
          </div>
        </div>
      )}

      {step === "questions" && language && (
        <Questionnaire
          questions={questions}
          languageName={language.name}
          onSubmit={submit}
          onBack={() => setStep("language")}
          busy={busy}
        />
      )}

      {step === "results" && result && (
        <Results
          data={result}
          answers={answers}
          onRestart={() => {
            setResult(null);
            setStep("language");
          }}
        />
      )}

      <footer className="muted">
        Frequency data from the <code>wordfreq</code> corpus · glue words and
        topic vocabulary are hand-curated.
      </footer>
    </div>
  );
}
