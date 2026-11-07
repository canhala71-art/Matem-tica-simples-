import { Component, type ReactNode } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { AuthProvider } from './lib/auth';
import { Layout, RequireAdmin, RequireAuth } from './components/Layout';
import { useAuth } from './lib/auth';
import { Landing } from './pages/Landing';
import { PlansPage } from './pages/Plans';
import { ActivatePage } from './pages/Activate';
import { SubscriptionPage } from './pages/Subscription';
import { QuizPage } from './pages/Quiz';
import { AuthPage, ResetPasswordPage } from './pages/Auth';
import { Dashboard } from './pages/Dashboard';
import { Academy, LevelPage, SubjectPage } from './pages/Academy';
import { LessonPage } from './pages/Lesson';
import { TestPage } from './pages/TestPage';
import { TeacherPage } from './pages/Teacher';
import { LabPage } from './pages/Lab';
import { AdminPage } from './pages/Admin';
import { NotFound } from './pages/NotFound';

class ErrorBoundary extends Component<{ children: ReactNode }, { failed: boolean }> {
  state = { failed: false };
  static getDerivedStateFromError() { return { failed: true }; }
  componentDidCatch(error: unknown) { console.error('Erro na interface:', error); }
  render() {
    if (!this.state.failed) return this.props.children;
    return (
      <div className="mx-auto max-w-md p-8 text-center">
        <p className="mb-4 font-semibold">Algo correu mal.</p>
        <button className="btn" onClick={() => window.location.assign('/')}>Recarregar</button>
      </div>
    );
  }
}

function Home() {
  const { session, loading } = useAuth();
  if (loading) return <p className="p-8 text-center muted">A carregar…</p>;
  return session ? <Layout><Dashboard /></Layout> : <Landing />;
}

export default function App() {
  return (
    <ErrorBoundary>
      <BrowserRouter>
        <AuthProvider>
          <Routes>
            <Route path="/entrar" element={<AuthPage />} />
            <Route path="/redefinir" element={<ResetPasswordPage />} />
            <Route index element={<Home />} />
            <Route element={<RequireAuth />}>
              <Route path="/quiz" element={<QuizPage />} />
              <Route path="/planos" element={<PlansPage />} />
              <Route path="/ativar" element={<ActivatePage />} />
              <Route path="/assinatura" element={<SubscriptionPage />} />
              <Route path="/academia" element={<Academy />} />
              <Route path="/academia/:levelSlug" element={<LevelPage />} />
              <Route path="/academia/:levelSlug/:subjectSlug" element={<SubjectPage />} />
              <Route path="/aula/:slug" element={<LessonPage />} />
              <Route path="/teste/:scope" element={<TestPage />} />
              <Route path="/professor" element={<TeacherPage />} />
              <Route path="/laboratorio" element={<LabPage />} />
              <Route element={<RequireAdmin />}>
                <Route path="/admin" element={<AdminPage />} />
              </Route>
            </Route>
            <Route path="*" element={<NotFound />} />
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </ErrorBoundary>
  );
}
