import type { Answers, Language, Question, WordListResponse } from "./types";

const BASE = import.meta.env.VITE_API_BASE ?? "";

async function get<T>(path: string): Promise<T> {
  const res = await fetch(`${BASE}${path}`);
  if (!res.ok) throw new Error(`${path} failed: ${res.status}`);
  return res.json();
}

export function getLanguages() {
  return get<Language[]>("/api/languages");
}

export async function getQuestions() {
  const data = await get<{ questions: Question[] }>("/api/questionnaire");
  return data.questions;
}

export async function buildWordList(
  language: string,
  answers: Answers
): Promise<WordListResponse> {
  const res = await fetch(`${BASE}/api/wordlist`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ language, answers }),
  });
  if (!res.ok) throw new Error(`wordlist failed: ${res.status}`);
  return res.json();
}

export function wordListCsvUrl() {
  return `${BASE}/api/wordlist.csv`;
}

export async function downloadCsv(language: string, answers: Answers) {
  const res = await fetch(`${BASE}/api/wordlist.csv`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ language, answers }),
  });
  if (!res.ok) throw new Error(`csv failed: ${res.status}`);
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `first-1000-${language}.csv`;
  a.click();
  URL.revokeObjectURL(url);
}
