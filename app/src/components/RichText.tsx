import { Fragment, useMemo } from 'react';
import katex from 'katex';
import 'katex/dist/katex.min.css';

function tex(src: string, display: boolean): string {
  return katex.renderToString(src, { displayMode: display, throwOnError: false, trust: false, strict: 'ignore' });
}

/** Texto com fórmulas KaTeX ($...$ e $$...$$) e **negrito**. O resto é texto simples (sem HTML). */
export function RichText({ text, className = '' }: { text: string; className?: string }) {
  const paragraphs = useMemo(() => text.split(/\n{2,}/), [text]);
  return (
    <div className={`space-y-3 leading-relaxed ${className}`}>
      {paragraphs.map((para, i) => (
        <p key={i}>
          {para.split(/(\$\$[\s\S]+?\$\$|\$[^$\n]+?\$)/g).map((part, j) => {
            if (part.startsWith('$$') && part.endsWith('$$') && part.length > 4) {
              return <span key={j} className="block overflow-x-auto py-1" dangerouslySetInnerHTML={{ __html: tex(part.slice(2, -2), true) }} />;
            }
            if (part.startsWith('$') && part.endsWith('$') && part.length > 2) {
              return <span key={j} dangerouslySetInnerHTML={{ __html: tex(part.slice(1, -1), false) }} />;
            }
            return (
              <Fragment key={j}>
                {part.split(/(\*\*[^*]+\*\*)/g).map((s, k) =>
                  s.startsWith('**') && s.endsWith('**') && s.length > 4
                    ? <strong key={k}>{s.slice(2, -2)}</strong>
                    : <Fragment key={k}>{s}</Fragment>,
                )}
              </Fragment>
            );
          })}
        </p>
      ))}
    </div>
  );
}
