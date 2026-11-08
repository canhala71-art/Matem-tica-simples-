import { useMemo, useRef, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { makeRound, MATCH_SLUGS } from '../lib/matching';
import { saveRun } from '../lib/toolRuns';

const shuffle = <T,>(a: T[]) => { const r = [...a]; for (let i = r.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [r[i], r[j]] = [r[j], r[i]]; } return r; };

export function MatchPage() {
  const { slug = '' } = useParams();
  const [round, setRound] = useState(0);
  const pairs = useMemo(() => makeRound(slug), [slug, round]);
  const rights = useMemo(() => shuffle(pairs.map((p) => p.right)), [pairs]);
  const [sel, setSel] = useState<number | null>(null);
  const [links, setLinks] = useState<Record<number, string>>({});
  const [checked, setChecked] = useState(false);
  const [saveMsg, setSaveMsg] = useState<string | null>(null);
  const started = useRef(Date.now());

  if (!MATCH_SLUGS.includes(slug)) return <div className="card">Esta disciplina ainda não tem jogo de associação. <Link to="/academia" className="underline">Voltar</Link></div>;

  const used = new Set(Object.values(links));
  const done = Object.keys(links).length === pairs.length;
  const score = pairs.filter((p, i) => links[i] === p.right).length;

  function pickRight(r: string) {
    if (checked || sel === null || used.has(r)) return;
    setLinks((l) => ({ ...l, [sel]: r }));
    setSel(null);
  }
  function unlink(i: number) {
    if (checked) return;
    setLinks((l) => { const n = { ...l }; delete n[i]; return n; });
  }
  async function check() {
    setChecked(true);
    const err = await saveRun('associacao', `Associação · ${slug}`, score, pairs.length, Math.round((Date.now() - started.current) / 1000));
    setSaveMsg(err ?? 'Resultado guardado.');
  }
  function again() {
    setLinks({}); setSel(null); setChecked(false); setSaveMsg(null); started.current = Date.now(); setRound((x) => x + 1);
  }

  return (
    <div className="space-y-4">
      <Link to="/academia" className="muted">← Academia</Link>
      <h1 className="text-2xl font-bold">Jogo de associação</h1>
      <p className="muted">Toca numa conta à esquerda e depois no resultado certo à direita. Toca numa conta já ligada para a desligar.</p>
      <div className="grid grid-cols-2 gap-3">
        <div className="space-y-2">
          {pairs.map((p, i) => {
            const ok = checked && links[i] === p.right;
            const bad = checked && links[i] !== p.right;
            return (
              <button key={i} onClick={() => (links[i] !== undefined ? unlink(i) : setSel(i))}
                className={`btn-ghost w-full justify-between ${sel === i ? 'border-electric-500 bg-electric-500/10' : ''} ${ok ? 'border-emerald-500' : ''} ${bad ? 'border-red-500' : ''}`}>
                <span>{p.left}</span><span className="font-semibold">{links[i] ?? '?'}</span>
              </button>
            );
          })}
        </div>
        <div className="space-y-2">
          {rights.map((r) => (
            <button key={r} disabled={used.has(r) || checked || sel === null} onClick={() => pickRight(r)} className="btn-ghost w-full">{r}</button>
          ))}
        </div>
      </div>
      {!checked && <button className="btn w-full" disabled={!done} onClick={() => void check()}>Verificar</button>}
      {checked && (
        <div className="card space-y-2">
          <p className="font-semibold">{score}/{pairs.length} certas.</p>
          {pairs.filter((p, i) => links[i] !== p.right).map((p, i) => <p key={i} className="text-sm">{p.left} = <strong>{p.right}</strong></p>)}
          {saveMsg && <p className="muted text-sm">{saveMsg}</p>}
          <button className="btn w-full" onClick={again}>Jogar outra vez</button>
        </div>
      )}
    </div>
  );
}
