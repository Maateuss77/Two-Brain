// App.js
import { useState } from 'react';
import './App.css';
import MainAppLayout from './components/MainAppLayout';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    if (username === 'test' && password === 'password') {
      setIsLoggedIn(true);
      alert('Login bem-sucedido!');
    } else {
      alert('Credenciais inválidas. Use "test" e "password".');
    }
  };

  if (isLoggedIn) {
    return <MainAppLayout/>;
  }

  return (
    <div className="App">
      <div className="login-container">
        <h1>Two Brain - Login</h1>
        <form onSubmit={handleLogin} className="login-form">
          <div className="form-group">
            <label htmlFor="username">Usuário:</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Senha:</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="login-button">Entrar</button>
        </form>
      </div>
    </div>
  );
}

// const MainAppPrototype = () => {
//   return (
//     <div className="App">
//       <header className="app-header">
//         <h1>Two Brain</h1>
//         <nav>
//           <ul>
//             <li><a href="#dashboard">Dashboard</a></li>
//             <li><a href="#notes">Minhas Notas</a></li>
//             <li><a href="#graph">Grafo de Conexões</a></li>
//             <li><a href="#settings">Configurações</a></li>
//             <li><button onClick={() => window.location.reload()} className="logout-button">Sair</button></li>
//           </ul>
//         </nav>
//       </header>
//       <div className="app-content">
//         <h2>Bem-vindo ao Two Brain!</h2>
//         <p>Este é o protótipo da sua interface principal.</p>
//         {/* Placeholder para o conteúdo */}
//         <div className="main-area-placeholder">
//           <h3>Seu espaço de trabalho</h3>
//           <p>Imagine aqui suas notas, editor, e o grafo de conexões.</p>
//           <div className="feature-card">
//             <h4>Crie uma Nova Nota</h4>
//             <p>Comece a registrar suas ideias.</p>
//             <button>Nova Nota</button>
//           </div>
//           <div className="feature-card">
//             <h4>Explore o Grafo</h4>
//             <p>Veja como suas ideias se conectam visualmente.</p>
//             <button>Ver Grafo</button>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// };

export default App;