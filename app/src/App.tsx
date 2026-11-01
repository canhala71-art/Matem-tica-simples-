import { Component, type ReactNode } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { AuthProvider } from './lib/auth';
import { RequireAdmin, RequireAuth } from './components/Layout';
import { AuthPage, ResetPasswordPage } from './pages/Auth';
import { Dashboard } from './pages/Dashboard';
import { Academy, LevelPage, SubjectPage } from './pages/Academy';
import { LessonPage } from './pages/Lesson';
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

export default function App() {
  return (
    <ErrorBoundary>
      <BrowserRouter>
        <AuthProvider>
          <Routes>
            <Route path="/entrar" element={<AuthPage />} />
            <Route path="/redefinir" element={<ResetPasswordPage />} />
            <Route element={<RequireAuth />}>
              <Route index element={<Dashboard />} />
              <Route path="/academia" element={<Academy />} />
              <Route path="/academia/:levelSlug" element={<LevelPage />} />
              <Route path="/academia/:levelSlug/:subjectSlug" element={<SubjectPage />} />
              <Route path="/aula/:slug" element={<LessonPage />} />
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
