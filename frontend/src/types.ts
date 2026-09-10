export interface Language {
  code: string;
  name: string;
}

export interface QOption {
  id: string;
  label: string;
  weights: Record<string, number>;
}

export interface Question {
  id: string;
  prompt: string;
  help?: string;
  multi: boolean;
  options: QOption[];
}

export interface WordEntry {
  rank: number;
  word: string;
  gloss: string;
  topics: string[];
  topic_labels: string[];
  zipf: number;
}

export interface MandatoryEntry {
  word: string;
  gloss: string;
  zipf: number;
}

export interface TopicRef {
  id: string;
  label: string;
}

export interface WordListResponse {
  language: string;
  language_name: string;
  core_size: number;
  profile: Record<string, number>;
  topics_covered: TopicRef[];
  focus_topics: TopicRef[];
  mandatory: MandatoryEntry[];
  core: WordEntry[];
}

export type Answers = Record<string, string[]>;
