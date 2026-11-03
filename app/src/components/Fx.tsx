import { useEffect, useMemo, useState } from 'react';

const COLORS = ['#2f6bff', '#a78bfa', '#10b981', '#f59e0b', '#ef4444', '#06b6d4'];

/** Chuva de confetis (só decorativa). Desaparece sozinha ao fim de ~3 s. */
export function Confetti({ pieces = 48 }: { pieces?: number }) {
  const [alive, setAlive] = useState(true);
  const items = useMemo(
    () => Array.from({ length: pieces }, (_, i) => ({
      left: Math.random() * 100, delay: Math.random() * 0.6, dur: 1.8 + Math.random() * 1.4,
      color: COLORS[i % COLORS.length], key: i,
    })),
    [pieces],
  );
  useEffect(() => { const t = setTimeout(() => setAlive(false), 3600); return () => clearTimeout(t); }, []);
  if (!alive) return null;
  return (
    <div aria-hidden="true">
      {items.map((p) => (
        <span key={p.key} className="confetti-piece"
          style={{ left: `${p.left}%`, background: p.color, animationDelay: `${p.delay}s`, animationDuration: `${p.dur}s` }} />
      ))}
    </div>
  );
}

/** Número que sobe suavemente até ao valor final. */
export function useCountUp(target: number, ms = 900): number {
  const [v, setV] = useState(0);
  useEffect(() => {
    let raf = 0;
    const t0 = performance.now();
    const tick = (now: number) => {
      const p = Math.min(1, (now - t0) / ms);
      setV(Math.round(target * (1 - Math.pow(1 - p, 3))));
      if (p < 1) raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [target, ms]);
  return v;
}

/** Anel de progresso animado (percentagem 0-100). */
export function ProgressRing({ percent, size = 120 }: { percent: number; size?: number }) {
  const shown = useCountUp(percent);
  const r = (size - 14) / 2;
  const c = 2 * Math.PI * r;
  const [go, setGo] = useState(false);
  useEffect(() => { const t = setTimeout(() => setGo(true), 60); return () => clearTimeout(t); }, []);
  const color = percent >= 75 ? '#10b981' : percent >= 50 ? '#2f6bff' : '#f59e0b';
  return (
    <div className="relative mx-auto" style={{ width: size, height: size }} role="img" aria-label={`${percent}% de acertos`}>
      <svg width={size} height={size} className="-rotate-90">
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke="currentColor" strokeOpacity={0.12} strokeWidth={10} />
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke={color} strokeWidth={10} strokeLinecap="round"
          strokeDasharray={c} strokeDashoffset={go ? c * (1 - percent / 100) : c}
          style={{ transition: 'stroke-dashoffset 1s cubic-bezier(.22,1,.36,1)' }} />
      </svg>
      <span className="absolute inset-0 flex items-center justify-center text-2xl font-extrabold">{shown}%</span>
    </div>
  );
}

let audio: AudioContext | null = null;
/** Sons curtos opcionais (WebAudio, sem ficheiros). Falha em silêncio. */
export function playTone(kind: 'ok' | 'bad' | 'win') {
  try {
    const Ctx = window.AudioContext ?? (window as unknown as { webkitAudioContext?: typeof AudioContext }).webkitAudioContext;
    if (!Ctx) return;
    audio = audio ?? new Ctx();
    const seq: [number, number][] = kind === 'ok' ? [[660, 0], [880, 0.11]] : kind === 'win' ? [[523, 0], [659, 0.12], [784, 0.24], [1047, 0.36]] : [[190, 0]];
    for (const [f, at] of seq) {
      const o = audio.createOscillator();
      const g = audio.createGain();
      o.type = kind === 'bad' ? 'sawtooth' : 'sine';
      o.frequency.value = f;
      g.gain.setValueAtTime(0.0001, audio.currentTime + at);
      g.gain.exponentialRampToValueAtTime(0.12, audio.currentTime + at + 0.02);
      g.gain.exponentialRampToValueAtTime(0.0001, audio.currentTime + at + (kind === 'bad' ? 0.28 : 0.16));
      o.connect(g); g.connect(audio.destination);
      o.start(audio.currentTime + at);
      o.stop(audio.currentTime + at + 0.3);
    }
  } catch { /* sem áudio: ignora */ }
}

export function buzz(ms: number) {
  try { navigator.vibrate?.(ms); } catch { /* ignora */ }
}
