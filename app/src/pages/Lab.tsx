import { useEffect, useMemo, useRef, useState } from 'react';
import { evaluate, parse, variables, type Ast } from '@shared/math-validator';

const PRESETS = ['a*x^2 + b*x + c', 'a*sin(b*x + c)', 'a*x + b', 'sqrt(x) * a', 'a/x + b'];

export function LabPage() {
  const [expr, setExpr] = useState(PRESETS[0]);
  const [a, setA] = useState(1);
  const [b, setB] = useState(0);
  const [c, setC] = useState(-2);
  const [range, setRange] = useState(6);
  const canvas = useRef<HTMLCanvasElement>(null);

  const parsed = useMemo<{ ast: Ast | null; error: string | null }>(() => {
    try {
      const ast = parse(expr);
      const extra = [...variables(ast)].filter((v) => !['x', 'a', 'b', 'c'].includes(v));
      if (extra.length) return { ast: null, error: `Variável desconhecida: ${extra.join(', ')} (usa x, a, b, c)` };
      return { ast, error: null };
    } catch {
      return { ast: null, error: 'Expressão inválida. Exemplo: a*x^2 + b*x + c' };
    }
  }, [expr]);

  useEffect(() => {
    const cv = canvas.current;
    if (!cv) return;
    const dpr = window.devicePixelRatio || 1;
    const w = cv.clientWidth, h = cv.clientHeight;
    cv.width = w * dpr; cv.height = h * dpr;
    const ctx = cv.getContext('2d');
    if (!ctx) return;
    ctx.scale(dpr, dpr);
    const dark = document.documentElement.classList.contains('dark');
    ctx.clearRect(0, 0, w, h);
    const R = range;
    const sx = (x: number) => ((x + R) / (2 * R)) * w;
    const sy = (y: number) => h / 2 - (y / R) * (h / 2);

    ctx.lineWidth = 1;
    ctx.strokeStyle = dark ? '#1b3a7a' : '#e2e8f0';
    for (let i = -Math.floor(R); i <= Math.floor(R); i++) {
      ctx.beginPath(); ctx.moveTo(sx(i), 0); ctx.lineTo(sx(i), h); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(0, sy(i)); ctx.lineTo(w, sy(i)); ctx.stroke();
    }
    ctx.strokeStyle = dark ? '#94a3b8' : '#475569';
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(0, sy(0)); ctx.lineTo(w, sy(0)); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(sx(0), 0); ctx.lineTo(sx(0), h); ctx.stroke();

    if (!parsed.ast) return;
    ctx.strokeStyle = '#2f6bff';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    let pen = false;
    let prevY = 0;
    const steps = Math.max(200, Math.floor(w));
    for (let i = 0; i <= steps; i++) {
      const x = -R + (2 * R * i) / steps;
      const y = evaluate(parsed.ast, { x, a, b, c });
      const visible = Number.isFinite(y) && Math.abs(y) < R * 4;
      if (!visible || (pen && Math.abs(y - prevY) > R * 2)) { pen = false; prevY = y; continue; } // assíntotas
      if (!pen) { ctx.moveTo(sx(x), sy(y)); pen = true; } else ctx.lineTo(sx(x), sy(y));
      prevY = y;
    }
    ctx.stroke();
  }, [parsed, a, b, c, range]);

  const slider = (label: string, v: number, set: (n: number) => void) => (
    <label className="block text-sm">
      <span className="font-medium">{label} = {v}</span>
      <input type="range" min={-5} max={5} step={0.1} value={v} onChange={(e) => set(Number(e.target.value))} className="w-full" />
    </label>
  );

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Laboratório matemático</h1>
      <p className="muted">Escreve uma função de x e mexe nos parâmetros a, b e c para ver o gráfico mudar.</p>
      <div className="card space-y-3">
        <label className="block text-sm font-medium">f(x) =
          <input className="input mt-1 font-mono" value={expr} onChange={(e) => setExpr(e.target.value)} spellCheck={false} autoCapitalize="off" />
        </label>
        <div className="flex flex-wrap gap-2">
          {PRESETS.map((p) => <button key={p} className="btn-ghost !px-2.5 !py-1.5 font-mono text-xs" onClick={() => setExpr(p)}>{p}</button>)}
        </div>
        {parsed.error && <p role="alert" className="text-sm text-red-600">{parsed.error}</p>}
        <div className="grid gap-3 sm:grid-cols-4">
          {slider('a', a, setA)}{slider('b', b, setB)}{slider('c', c, setC)}
          <label className="block text-sm">
            <span className="font-medium">Zoom: de −{range} a {range}</span>
            <input type="range" min={2} max={20} step={1} value={range} onChange={(e) => setRange(Number(e.target.value))} className="w-full" />
          </label>
        </div>
      </div>
      <canvas ref={canvas} className="card aspect-square w-full !p-0 sm:aspect-[16/10]" role="img" aria-label={`Gráfico de f(x) = ${expr}`} />
    </div>
  );
}
