import { useState } from 'react';
import { LogIn, UserPlus, Mail, Lock } from 'lucide-react';

const Login = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);
    
    try {
      // Simulate API call - in real implementation, this would call backend
      // For now, we'll simulate a successful login after 1 second
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Simple validation for demo
      if (!email || !password) {
        throw new Error('Email e senha são obrigatórios');
      }
      
      // In real app, would verify credentials with backend
      // For demo, accept any non-empty email/password
      const user = {
        id: 1,
        email: email,
        name: email.split('@')[0]
      };
      
      onLogin(user);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#0f0f12] flex items-center justify-center p-4">
      <div className="w-full max-w-md space-y-6">
        <div className="space-y-4 text-center">
          <h1 className="text-2xl font-bold text-white">
            Flow AI
          </h1>
          <p className="text-lg text-gray-400">
            Entrar na sua conta
          </p>
        </div>
        
        <form onSubmit={handleSubmit} className="space-y-5">
          <div className="space-y-3">
            <label className="block text-sm font-medium text-gray-300">
              Email
            </label>
            <div className="flex items-center border border-gray-700 rounded-xl px-3 py-2">
              <Mail className="h-4 w-4 text-gray-500 mr-2" />
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="seu@email.com"
                className="flex-1 bg-transparent text-white outline-none"
                autoFocus
                required
              />
            </div>
          </div>
          
          <div className="space-y-3">
            <label className="block text-sm font-medium text-gray-300">
              Senha
            </label>
            <div className="flex items-center border border-gray-700 rounded-xl px-3 py-2">
              <Lock className="h-4 w-4 text-gray-500 mr-2" />
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                className="flex-1 bg-transparent text-white outline-none"
                required
              />
            </div>
          </div>
          
          {error && (
            <div className="bg-red-900/20 border border-red-500/30 text-red-400 px-4 py-3 rounded-xl">
              {error}
            </div>
          )}
          
          <button
            type="submit"
            disabled={loading}
            className="w-full flex items-center justify-center bg-gradient-to-r from-[#8b5cf6] to-[#06b6d4] text-white font-semibold py-3 px-4 rounded-xl transition-all duration-200 hover:from-[#7c3aed] hover:to:#059669 disabled:opacity-50"
          >
            {loading ? (
              <>
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"></path>
                </svg>
                Entrando...
              </>
            ) : (
              <>
                <LogIn className="mr-2 h-4 w-4" />
                Entrar
              </>
            )}
          </button>
        </form>
        
        <div className="text-center text-sm text-gray-500">
          <button
            onClick={() => {}}
            className="underline hover:text-gray-300"
          >
            Esqueceu a senha?
          </button>
        </div>
        
        <div className="text-center text-xs text-gray-600">
          Não tem uma conta?{" "}
          <button
            onClick={() => {}}
            className="font-medium text-cyan-400 hover:text-cyan-300"
          >
            Criar conta
          </button>
        </div>
      </div>
    </div>
  );
};

export default Login;
