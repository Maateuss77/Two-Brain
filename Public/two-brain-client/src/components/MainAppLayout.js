// MainAppLayout.js (Um componente mais complexo para a interface principal)
import { useState } from 'react';
import './MainAppLayout.css'; // Usaremos um novo CSS para isso

const MainAppLayout = () => {
  const [selectedNote, setSelectedNote] = useState(null);
  const notes = [
    { id: 1, title: "Ideia para Projeto X", content: "Primeira ideia para o projeto X. Conectar com [[Brainstorm]] e [[Reunião Inicial]]." },
    { id: 2, title: "Brainstorm de Features", content: "Lista de features: autenticação, CRUD de notas, visualização de grafo. Ver [[Ideia para Projeto X]]." },
    { id: 3, title: "Notas de Reunião Inicial", content: "Pontos discutidos: escopo, equipe, prazos. Menciona [[Ideia para Projeto X]]." },
    { id: 4, title: "Conceito de Grafo", content: "Como visualizar as conexões entre as notas. Influências do [[Obsidian Graph]]." },
  ];

  return (
    <div className="app-container">
      {/* Top Bar / Header */}
      <header className="app-header-main">
        <h1 className="app-title">Two Brain</h1>
        <div className="search-bar">
          <input type="text" placeholder="Pesquisar notas..." />
          <button>🔍</button>
        </div>
        <nav className="main-nav">
          <button>➕ Nova Nota</button>
          <button>⚙️ Configurações</button>
          <button onClick={() => alert('Saindo...')} className="logout-btn">🚪 Sair</button>
        </nav>
      </header>

      <div className="main-layout">
        {/* Left Sidebar - Navigation */}
        <aside className="sidebar left-sidebar">
          <h3>Minhas Notas</h3>
          <ul className="note-list">
            {notes.map(note => (
              <li 
                key={note.id} 
                className={selectedNote && selectedNote.id === note.id ? 'active' : ''}
                onClick={() => setSelectedNote(note)}
              >
                {note.title}
              </li>
            ))}
          </ul>
          <div className="tags-section">
            <h3>Tags</h3>
            <div className="tag-cloud">
              <span className="tag">#projeto</span>
              <span className="tag">#ideias</span>
              <span className="tag">#reuniao</span>
              <span className="tag">#dev</span>
            </div>
          </div>
        </aside>

        {/* Central Content Area - Note Editor */}
        <main className="content-area">
          {selectedNote ? (
            <div className="note-editor">
              <h2>{selectedNote.title}</h2>
              <textarea 
                className="markdown-editor"
                value={selectedNote.content}
                onChange={(e) => { /* Em um app real, atualizaria o estado da nota */ }}
                placeholder="Comece a escrever aqui..."
              />
              <div className="editor-toolbar">
                <button>B</button>
                <button>_I_</button>
                <button>H1</button>
                <button>Link</button>
                <button>Gravar</button>
              </div>
            </div>
          ) : (
            <div className="empty-state">
              <h3>Selecione uma nota ou crie uma nova.</h3>
              <button>➕ Criar Nova Nota</button>
            </div>
          )}
        </main>

        {/* Right Sidebar - Graph / Context */}
        <aside className="sidebar right-sidebar">
          <h3>Grafo de Conexões</h3>
          <div className="graph-preview-placeholder">
            {/* Imagine um componente de grafo aqui, como D3.js ou Cytoscape.js */}
            <p>Visualização das conexões da nota atual:</p>
            <div className="graph-node main-node">{selectedNote ? selectedNote.title : 'Nenhuma Nota'}</div>
            <div className="graph-links">
              {selectedNote && selectedNote.content.match(/\[\[(.*?)\]\]/g)?.map((link, index) => (
                <div key={index} className="graph-node linked-node">{link.replace(/\[\[|\]\]/g, '')}</div>
              ))}
            </div>
          </div>
          <button className="full-graph-button">Ver Grafo Completo</button>
        </aside>
      </div>
    </div>
  );
};

export default MainAppLayout;