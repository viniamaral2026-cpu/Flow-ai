import { useState, useEffect, useRef } from 'react'
import { Mic, MessageSquare, Calendar, Eye, Settings, Terminal, Home, Power, Send, Zap, Plus, Play, Square, Trash2, Music, Timer, Radar, Brain, Sparkles, AlarmClock, ChefHat, RotateCw, X, Link2, CloudSun, Gauge, ShoppingCart, NotebookPen, Wrench, ClipboardCopy, LogIn, UserPlus, Folder, Search } from 'lucide-react'

const screens = [
  { id: 'home', label: 'Principal', icon: Home },
  { id: 'chat', label: 'Conversas', icon: MessageSquare },
  { id: 'acao', label: 'Ver e Agir', icon: Radar },
  { id: 'timers', label: 'Timers e Alarmes', icon: AlarmClock },
  { id: 'receitas', label: 'Receitas', icon: ChefHat },
  { id: 'musica', label: 'Música', icon: Music },
  { id: 'arquivos', label: 'Arquivos', icon: Folder },
  { id: 'foco', label: 'Modo Foco', icon: Timer },
  { id: 'integracoes', label: 'Integrações', icon: CloudSun },
  { id: 'rotinas', label: 'Rotinas', icon: Wrench },
  { id: 'tasks', label: 'Autônomas', icon: Calendar },
  { id: 'vision', label: 'Visão', icon: Eye },
  { id: 'settings', label: 'Configurações', icon: Settings },
  { id: 'logs', label: 'Logs', icon: Terminal },
]

function now(){ return new Date().toLocaleTimeString().slice(0,5) }

export default function App(){
  const [active, setActive] = useState('home');
  const [listening, setListening] = useState(false);
const [messages, setMessages] = useState([
     { role:'flow', text:'Olá! Sou a Flow. Pode falar ou digitar. No menu, em "Ver e Agir" eu abro, clico e digito na tela por você.', time: now() }
   ]);
  const [input, setInput] = useState('');
  const [busy, setBusy] = useState(false);

  const [tasks, setTasks] = useState([]);
  const [taskForm, setTaskForm] = useState({ title:'', command:'', intervalo:5, hora:'', active:true });
  const [logs, setLogs] = useState([]);
  const [visionData, setVisionData] = useState(null);
  const [visionPergunta, setVisionPergunta] = useState('Descreva tudo que você vê na tela e quais aplicações estão abertas');
  const [settings, setSettings] = useState({ model:'strong', autonomy:true });
   
   // Authentication state
   const [isAuthenticated, setIsAuthenticated] = useState(false);
   const [user, setUser] = useState(null);
   const [authMode, setAuthMode] = useState('login'); // 'login' or 'register'
   const [authForm, setAuthForm] = useState({ email: '', password: '', confirmPassword: '' });
   const [authLoading, setAuthLoading] = useState(false);
   const [authError, setAuthError] = useState(null);

  const [acaoPrompt, setAcaoPrompt] = useState('Abra o YouTube e pesquise por lofi para focar');
  const [acaoResult, setAcaoResult] = useState(null);
  const [acaoBusy, setAcaoBusy] = useState(false);
  const [digTela, setDigTela] = useState('');

  const [players, setPlayers] = useState([]);
  const [sons, setSons] = useState([]);
  const [musicaQuery, setMusicaQuery] = useState('');
  const [volume, setVolume] = useState(50);
  const [musicaMsg, setMusicaMsg] = useState('');

  const [foco, setFoco] = useState(null);
  const [focoMin, setFocoMin] = useState(25);

  const [timers, setTimers] = useState([]);
  const [timerForm, setTimerForm] = useState({ nome:'', min:5 });

  const [receitaQuery, setReceitaQuery] = useState('');
  const [receitas, setReceitas] = useState([]);
  const [receitaBusy, setReceitaBusy] = useState(false);
  const [receitaSite, setReceitaSite] = useState('todos');

  const [agora, setAgora] = useState(null);
  const [locais, setLocais] = useState([]);
  const [localQuery, setLocalQuery] = useState('');
  const [notas, setNotas] = useState([]);
  [comprasItem, setComprasItem] = useState('');
  [notaTexto, setNotaTexto] = useState('');
  [brilhoVal, setBrilhoVal] = useState(100);
  [waDest, setWaDest] = useState('');
  [waMsg, setWaMsg] = useState('');
  [integMsg, setIntegMsg] = useState('');
  [rotinas, setRotinas] = useState([]);
  [rotinaForm, setRotinaForm] = useState({ nome:'', passos:[{tipo:'notificacao', valor:''}] });
  [rotinaMsg, setRotinaMsg] = useState('');
  [memTexto, setMemTexto] = useState('');
  [memBusca, setMemBusca] = useState('');
  [memRes, setMemRes] = useState(null);
  [clima, setClima] = useState(null);
  [climaCidade, setClimaCidade] = useState('Taquara');
  [climaLoading, setClimaLoading] = useState(false);
  [sysInfo, setSysInfo] = useState(null);
  [compras, setCompras] = useState([]);
  const recorderRef = useRef(null);
  const chunksRef = useRef([]);
  const msgsRef = useRef(messages);
  
  useEffect(()=>{ msgsRef.current = messages }, [messages]);

  // ============= AUTENTICATION FUNCTIONS =============
  const handleAuthChange = (e) => {
    const { name, value } = e.target;
    setAuthForm(prev => ({ ...prev, [name]: value }));
  };

  const handleAuthSubmit = async (e) => {
    e.preventDefault();
    setAuthLoading(true);
    setAuthError(null);
    
    try {
      if (authMode === 'login') {
        if (!authForm.email || !authForm.password) {
          throw new Error('Email e senha são obrigatórios');
        }
        
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // Simple validation for demo
        const mockUser = {
          id: 1,
          email: authForm.email,
          name: authForm.email.split('@')[0]
        };
        
        setUser(mockUser);
        setIsAuthenticated(true);
        setAuthLoading(false);
      } else if (authMode === 'register') {
        if (!authForm.email || !authForm.password || !authForm.confirmPassword) {
          throw new Error('Todos os campos são obrigatórios');
        }
        
        if (authForm.password !== authForm.confirmPassword) {
          throw new Error('As senhas não coincidem');
        }
        
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        setAuthLoading(false);
        setAuthMode('login');
        setAuthForm({ email: '', password: '', confirmPassword: '' });
        alert('Registro exitoso! Por favor, faça login.');
      }
    } catch (error) {
      setAuthError(error.message);
      setAuthLoading(false);
    }
  };

  const handleLogout = () => {
    setUser(null);
    setIsAuthenticated(false);
    setAuthForm({ email: '', password: '', confirmPassword: '' });
    setAuthError(null);
  };

  // ============= APP FUNCTIONALITY (KEEPING EXISTING LOGIC) =============
  const playTTS = (texto) => {
    if(!texto) return;
    const a = new Audio(`/api/tts?text=` + encodeURIComponent(texto.slice(0,1000)));
    a.play().catch(()=>{});
  };

  const extractBash = (text='') => {
    const re = /```(?:bash|sh)?\s*([\s\S]*?)```/g; 
    const out=[]; 
    let m;
    while ((m=re.exec(text))) out.push(m[1].trim());
    return out;
  };

  const runCmd = async (cmd, idx) => {
    try {
      const r = await fetch('/api/execute', { 
        method:'POST', 
        headers:{'Content-Type':'application/json'}, 
        body: JSON.stringify({command:cmd}) 
      });
      const d = await r.json();
      setMessages(m=>m.map((x,j)=>j===idx?{...x, exec:d}:x));
    } catch(e) {
      setMessages(m=>m.map((x,j)=>j===idx?{...x, exec:{error:String(e)}}:x));
    }
  };

  const enviarTexto = async (pergunta) => {
    const hist = msgsRef.current
      .slice(0, -1)
      .filter(m=>m.role && m.text)
      .map(m=>({role:m.role==='user'?'user':'assistant', content:m.text}));
    const respIdx = msgsRef.current.length;
    const plh = [...msgsRef.current, {role:'flow', text:'', streaming:true, time:now()}];
    msgsRef.current = plh;
    setMessages(plh);
    const setMsg = (fn) => { 
      const next = fn(msgsRef.current); 
      msgsRef.current = next; 
      setMessages(next) 
    };
    try {
      const r = await fetch('/api/chat/stream', { 
        method:'POST', 
        headers:{'Content-Type':'application/json'}, 
        body: JSON.stringify({messages:[...hist, {role:'user',content:pergunta}], task:settings.model||'strong'}) 
      });
      if(!r.ok || !r.body) throw new Error('HTTP '+r.status);
      const reader = r.body.getReader();
      const dec = new TextDecoder();
      let full = '';
      while(true){
        const {done, value} = await reader.read();
        if(done) break;
        for(const ln of dec.decode(value, {stream:true}).split('\n\n')){
          if(!ln.startsWith('data: ')) continue;
          const payload = ln.slice(6);
          if(payload === '[DONE]') continue;
          try{
            const j = JSON.parse(payload);
            if(j.erro){ full = 'Erro: '+j.erro }
            else if(j.token){ full += j.token }
          }catch(_){}
        }
        setMsg(m=>m.map((x,i)=>i===respIdx?{...x, text:full, streaming:true}:x));
      }
      const final = full || '(sem resposta)';
      setMsg(m=>m.map((x,i)=>i===respIdx?{...x, text:final, streaming:false}:x));
      playTTS(final);
      return final;
    } catch(e) {
      setMsg(m=>m.map((x,i)=>i===respIdx?{...x, text:'Erro de conexão: '+String(e), streaming:false}:x));
      return null;
    }
  };

  const send = async () => {
    const texto = input;
    if(!texto?.trim() || busy) return;
    const pergunta = texto.trim();
    setInput('');
    setBusy(true);
    const nova = [...msgsRef.current, {role:'user', text:pergunta, time:now()}];
    msgsRef.current = nova;
    setMessages(nova);
    await enviarTexto(pergunta);
    setBusy(false);
  };

  const ouvir = async () => {
    if(listening) { 
      try{ recorderRef.current?.stop() } catch{}; 
      return; 
    }
    try {
      const stream = await navigator.mediaDevices.getUserMedia({audio:true});
      const rec = new MediaRecorder(stream);
      recorderRef.current = rec;
      chunksRef.current = [];
      rec.ondataavailable = e => chunksRef.current.push(e.data);
      rec.onstop = async () => {
        stream.getTracks().forEach(t=>t.stop());
        setListening(false);
        const blob = new Blob(chunksRef.current, {type:rec.mimeType});
        await enviarAudio(blob);
      };
      setListening(true);
      rec.start();
    } catch(e) {
      alert('Microfone não permitido: '+e.message);
    }
  };

  const enviarAudio = async (blob) => {
    setBusy(true);
    const fd = new FormData(); 
    fd.append('audio', blob, 'fala.webm');
    try {
      const r1 = await fetch('/api/listen', {method:'POST', body:fd});
      const t1 = await r1.json();
      const texto = (t1.text || '').trim();
      if(!texto) { setBusy(false); return }
      const nova = [...msgsRef.current, {role:'user', text:texto, time:now()}];
      msgsRef.current = nova;
      setMessages(nova);
      await enviarTexto(texto);
    } catch(e) {
      setMessages(prev=>[...prev, {role:'flow', text:'Erro ao processar áudio: '+String(e), time:now()}]);
    }
    setBusy(false);
  };

  const salvarSettings = async (patch) => {
    const s = {...settings, ...patch};
    setSettings(s);
    await fetch('/api/settings', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body:JSON.stringify(s) 
    });
  };

  // ============= TASKS FUNCTIONALITY =============
  const criarTask = async () => {
    if(!taskForm.title) return;
    const r = await fetch('/api/tasks', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body:JSON.stringify(taskForm) 
    });
    const d = await r.json(); 
    if(d.ok) fetchTasks();
  };
  const toggleTask = async (id) => { 
    await fetch(`/api/tasks/${id}/toggle`, {method:'POST'}); 
    fetchTasks() 
  };
  const runTask = async (id) => { 
    await fetch(`/api/tasks/${id}/run`, {method:'POST'}); 
    fetchTasks() 
  };
  const delTask = async (id) => { 
    if(!confirm('Remover tarefa?')) return; 
    await fetch(`/api/tasks/${id}`, {method:'DELETE'}); 
    fetchTasks() 
  };
  const fetchTasks = () => fetch('/api/tasks').then(r=>r.json()).then(d=>setTasks(d.tasks||[])).catch(()=>{});

  // ============= LOGS FUNCTIONALITY =============
  const fetchLogs = () => fetch('/api/logs').then(r=>r.json()).then(d=>setLogs(d.logs||[])).catch(()=>{});

  // ============= SETTINGS FUNCTIONALITY =============
  const fetchSettings = () => fetch('/api/settings').then(r=>r.json()).then(d=>setSettings(d)).catch(()=>{});

  // ============= FOCUS FUNCTIONALITY =============
  const fetchFoco = () => fetch('/api/system/focus/status').then(r=>r.json()).then(d=>setFoco(d)).catch(()=>{});
  const focoCmd = async (modo) => {
    const r = await fetch('/api/system/focus', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify(modo==='ativar'?{modo, min_:focoMin}:{modo}) 
    });
    const d = await r.json(); 
    setFoco(d);
    if(active==='foco') await fetchFoco();
  };

  // ============= TIMERS FUNCTIONALITY =============
  const fetchTimers = () => fetch('/api/timer').then(r=>r.json()).then(d=>setTimers(d.timers||[])).catch(()=>{});
  const criarTimer = async (nome, min) => {
    const seg = Math.max(1, Math.round((min || timerForm.min) * 60));
    const r = await fetch('/api/timer', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ nome: nome || timerForm.nome || 'alarme', segundos: seg }) 
    });
    const d = await r.json();
    if(d.ok) { 
      setTimers(d.timers || timers); 
      setTimerForm({ nome:'', min:5 }) 
    }
  };
  const cancelTimer = async id => {
    await fetch(`/api/timer/${id}/cancel`, { method:'POST' });
    fetchTimers();
  };

  // ============= MUSIC FUNCTIONALITY =============
  const atualizaMusica = () => {
    fetch('/api/musica/players').then(r=>r.json()).then(d=>setPlayers(d.players||[])).catch(()=>{});
    fetch('/api/musica/sons').then(r=>r.json()).then(d=>setSons(d.sons||[])).catch(()=>{});
    fetch('/api/musica/agora').then(r=>r.json()).then(d=>setAgora(d)).catch(()=>{});
    fetch('/api/musica/local').then(r=>r.json()).then(d=>setLocais(d.musicas||[])).catch(()=>{});
  };
  const musicaCmd = async (comando, extra={}) => {
    const r = await fetch('/api/musica', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({comando, ...extra}) 
    });
    const d = await r.json();
    setMusicaMsg(d.mensagem || d.error || JSON.stringify(d));
    atualizaMusica();
  };
  const tocarLocal = async (f) => {
    const d = await fetch('/api/musica', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({ comando:'tocar_local', query:f }) 
    }).then(x=>x.json());
    setMusicaMsg(d.msg || d.error || f);
  };

  // ============= MEMORY FUNCTIONALITY =============
  const memAprender = async () => {
    if(!memTexto.trim()) return;
    const r = await fetch('/api/memory/learn', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({texto:memTexto.trim()}) 
    });
    const d = await r.json();
    setMemRes({learned: d.ok, msg: d.ok?('Lembrei! ('+d.id+')'):(d.error||'erro')});
    setMemTexto('');
  };
  const memBuscar = async () => {
    if(!memBusca.trim()) return;
    const r = await fetch('/api/memory/search', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({pergunta:memBusca.trim(), k:4}) 
    });
    const d = await r.json();
    setMemRes({results: d.ok?d.resultados:(d.error||[])});
  };

  // ============= VISION FUNCTIONALITY =============
  const abrirVisao = async () => {
    setVisionData(null);
    try {
      const r = await fetch(`/api/vision?pergunta=`+encodeURIComponent(visionPergunta));
      const d = await r.json(); 
      setVisionData(d);
    } catch(e) { 
      setVisionData({error:String(e)}) 
    }
  };

  // ============= AÇÃO (VER E AGIR) FUNCTIONALITY =============
  const agir = async () => {
    if(!acaoPrompt.trim()) return;
    setAcaoBusy(true); 
    setAcaoResult(null);
    try {
      const r = await fetch('/api/vision/act', { 
        method:'POST', 
        headers:{'Content-Type':'application/json'}, 
        body: JSON.stringify({acao:'planejar', pergunta:acaoPrompt.trim()}) 
      });
      setAcaoResult(await r.json());
    } catch(e) { 
      setAcaoResult({ok:false, error:String(e)}) 
    }
    setAcaoBusy(false);
  };
  const digitarTela = async () => {
    if(!digTela.trim()) return;
    setAcaoBusy(true);
    try {
      const r = await fetch('/api/vision/act', { 
        method:'POST', 
        headers:{'Content-Type':'application/json'}, 
        body: JSON.stringify({acao:'digitar_tela', texto:digTela}) 
      });
      setAcaoResult(await r.json());
    } catch(e) { 
      setAcaoResult({ok:false, error:String(e)}) 
    }
    setDigTela(''); 
    setAcaoBusy(false);
  };

  // ============= INTEGRAÇÕES FUNCTIONALITY =============
  const fetchClima = async () => {
    setClimaLoading(true);
    try {
      const r = await fetch(`/api/integracoes/clima?cidade=`+encodeURIComponent(climaCidade));
      setClima(await r.json());
    } catch(e) { 
      setClima({ok:false, error:String(e)}) 
    }
    setClimaLoading(false);
  };
  const fetchSys = async () => { 
    try { 
      const r = await fetch('/api/integracoes/sistema'); 
      setSysInfo(await r.json()) 
    } catch(e){} 
  };
  const fetchCompras = async () => { 
    try { 
      const r = await fetch('/api/integracoes/compras'); 
      setCompras((await r.json()).items||[]) 
    } catch(e){} 
  };
  const fetchNotas = async () => { 
    try { 
      const r = await fetch('/api/integracoes/notas'); 
      setNotas((await r.json()).notas||[]) 
    } catch(e){} 
  };
  const addCompra = async () => {
    if(!comprasItem.trim()) return;
    const r = await fetch('/api/integracoes/compras', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({ acao:'adicionar', item:comprasItem.trim() }) 
    });
    setIntegMsg((await r.json()).mensagem||'');
    setComprasItem(''); 
    fetchCompras();
  };
  const delCompra = async (item) => {
    await fetch('/api/integracoes/compras', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({ acao:'remover', item }) 
    });
    fetchCompras();
  };
  const addNota = async () => {
    if(!notaTexto.trim()) return;
    await fetch('/api/integracoes/notas', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({ acao:'adicionar', texto:notaTexto.trim() }) 
    });
    setNotaTexto(''); 
    fetchNotas();
  };
  const delNota = async (id) => {
    await fetch('/api/integracoes/notas', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({ acao:'concluir', id }) 
    });
    fetchNotas();
  };
  const setBrilho = async (v) => {
    setBrilhoVal(v);
    await fetch('/api/integracoes/brilho', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({ nivel:v }) 
    });
  };
  const waEnviar = async () => {
    if(!waDest.trim() || !waMsg.trim()) return;
    const r = await fetch('/api/integracoes/whatsapp', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({ destinatario:waDest.trim(), mensagem:waMsg.trim() }) 
    });
    const d = await r.json();
    setIntegMsg(d.msg || d.error || '...');
    setWaMsg('');
  };
  const abrirSite = async (tipo) => {
    await fetch(`/api/integracoes/${tipo}/abrir`, { method:'POST' })
      .then(r=>r.json())
      .then(d=>setIntegMsg(d.msg||d.error||''))
      .catch(()=>{});
  };
  const gmailLer = async () => {
    const r = await fetch('/api/integracoes/gmail', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({ query:'is:unread', max:6 }) 
    });
    const d = await r.json();
    if(d.ok) 
      setIntegMsg((d.emails||[]).map(e=>`• ${e.de}: ${e.assunto}`).join('\n') || 'Caixa vazia (confira se o Gmail está logado no navegador).');
    else 
      setIntegMsg('Erro: ' + (d.error||''));
  };
  const fetchRotinas = async () => { 
    try { 
      const r = await fetch('/api/integracoes/rotinas'); 
      setRotinas((await r.json()).rotinas||[]) 
    } catch(e){} 
  };
  const addPasso = () => setRotinaForm(f=>({...f, passos:[...f.passos, {tipo:'notificacao', valor:''}]}));
  const setPasso = (i, p) => setRotinaForm(f=>({...f, passos:f.passos.map((x,j)=>j===i?{...x,...p}:x)}));
  const criarRotina = async () => {
    if(!rotinaForm.nome.trim()) return;
    const conv = {
      notificacao: p=>({tipo:'notificacao', mensagem:p.valor}),
      comando: p=>({tipo:'comando', cmd:p.valor}),
      esperar: p=>({tipo:'esperar', segundos:Number(p.valor)||2}),
      timer: p=>({tipo:'timer', nome:p.valor||rotinaForm.nome, segundos:300}),
      musica: p=>({tipo:'musica', acao:p.valor||'pause'}),
      clima: p=>({tipo:'clima', cidade:p.valor||'Taquara'}),
    };
    const passos = rotinaForm.passos.map(p=>conv[p.tipo]?conv[p.tipo](p):null).filter(Boolean);
    if(!passos.length) return;
    const r = await fetch('/api/integracoes/rotinas', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({ acao:'criar', nome:rotinaForm.nome.trim(), passos }) 
    });
    const d = await r.json();
    if(d.ok) 
      setRotinaMsg('Rotina "'+d.rotina.nome+'" criada com '+d.rotina.passos.length+' passos!');
    setRotinaForm({ nome:'', passos:[{tipo:'notificacao', valor:''}] });
    fetchRotinas();
  };
  const execRotina = async (nome) => {
    const r = await fetch('/api/integracoes/rotinas', { 
      method:'POST', 
      headers:{'Content-Type':'application/json'}, 
      body: JSON.stringify({ acao:'executar', nome }) 
    });
    const d = await r.json();
    if(d.ok) 
      setRotinaMsg('Executada:\n• '+ (d.resultados||[]).join('\n• '));
    else 
      setRotinaMsg(d.error||'');
  };
  const delRotina = async (nome) => {
    if(!confirm('Remover rotina '+nome+'?')) return;
    await fetch(`/api/integracoes/rotinas/${encodeURIComponent(nome)}`, { method:'DELETE' });
    fetchRotinas();
  };

  // ============= EFFECTS =============
  useEffect(() => {
    fetchTasks();
    fetchSettings();
    atualizaMusica();
  }, []);

  useEffect(() => {
    if(active==='tasks') fetchTasks();
    if(active==='logs') fetchLogs();
    if(active==='settings') fetchSettings();
    if(active==='musica') atualizaMusica();
    if(active==='foco') fetchFoco();
    if(active==='timers') fetchTimers();
    if(active==='integracoes') { 
      fetchClima(); 
      fetchSys(); 
      fetchCompras(); 
      fetchNotas(); 
      fetchRotinas() 
    }
    if(active==='rotinas') fetchRotinas();
  }, [active]);

  useEffect(() => {
    if(active==='timers' && timers.length) {
      const iv = setInterval(()=>setTick(t=>t+1), 1000);
      return ()=>clearInterval(iv);
    }
  }, [active, timers.length]);

  // ============= RENDER =============
  return (
    <div className="min-h-screen bg-[#0f0f12] text-white flex flex-col">
      {!isAuthenticated ? (
        // AUTHENTICATION VIEW
        <div className="flex-1 flex flex-col items-center justify-center p-6">
          {authMode === 'login' ? (
<Login onLogin={(user) => {
               setUser(user);
               setIsAuthenticated(true);
             }} />
          ) : (
<Register onRegister={(user) => {
               setUser(user);
               setIsAuthenticated(true);
             }} />
          )}
        </div>
      ) : (
        // MAIN APP VIEW (WHEN AUTHENTICATED)
        <>
          <div className="h-10 bg-[#1a1a23] flex items-center justify-between px-4 text-xs border-b border-white/10">
            <span className="font-bold">Flow AI — Assistente Autônomo</span>
            <div className="flex gap-3 items-center opacity-70">
              {foco?.ativo && <span className="text-orange-300">🔕 foco ativo{foco.timer?.faltando?` ${Math.ceil(foco.timer.faltando/60)}min`:''}</span>}
              <span>{now()} • {busy?'pensando...':'ok'}</span>
              <span>{settings.autonomy?'autôno on':'autôno off'}</span>
              <div className="flex items-center gap-2">
                <span className="text-sm">{user?.name || 'Usuário'}</span>
                <button onClick={handleLogout} className="text-xs text-red-400 hover:text-red-300">
                  Sair
                </button>
              </div>
            </div>
          </div>
          <div className="flex flex-1 overflow-hidden">
            <div className="w-[72px] bg-[#12121a] border-r border-white/10 flex flex-col items-center py-4 gap-3">
              {screens.map(s=>{const I=s.icon; return <button key={s.id} onClick={()=>setActive(s.id)} className={`w-12 h-12 rounded-xl flex items-center justify-center transition-all ${active===s.id?'bg-gradient-to-br from-[#8b5cf6] to-[#06b6d4] shadow-lg shadow-purple-500/30':'bg-white/5 hover:bg-white/10'}`} title={s.label}><I size={20}/></button>})}
            </div>
            <div className="flex-1 p-6 overflow-auto">
              {/* HOME SCREEN */}
              {active==='home' && (
                <div className="h-full flex flex-col items-center justify-center max-w-3xl mx-auto">
                  <div className="glass rounded-[32px] p-12 w-full text-center">
                    <button onClick={ouvir} className={`mx-auto w-64 h-64 rounded-full orb ${listening?'':'opacity-30'} flex items-center justify-center transition-all`}>
                      <div className={`w-56 h-56 rounded-full bg-black/40 flex items-center justify-center text-6xl ${listening?'animate-pulse':''}`}>{listening?<Mic size={60} className="text-cyan-300"/>:'✨'}</div>
                    </button>
                    <h2 className="mt-8 text-2xl font-light text-cyan-300">{listening?'Ouvindo...':'Toque no ícone para falar'}</h2>
                    <div className="mt-6 flex items-end justify-center gap-[3px] h-12">
                      {Array.from({length:64}).map((_,i)=><div key={i} className={`w-[3px] rounded-full ${listening?'bg-gradient-to-t from-[#8b5cf6] to-[#06b6d4] wave':'bg-white/20'}`} style={{animationDelay:`${i*0.02}s`, height:`${listening?8+Math.random()*28:4}px`}}/>)}
                    </div>
                    <p className="mt-3 text-sm opacity-60">{listening?'Detectando voz — fale agora':'Pressione o microfone ou digite abaixo'}</p>
                    <div className="mt-6 flex gap-2">
                      <input value={input} onChange={e=>setInput(e.target.value)} onKeyDown={e=>e.key==='Enter'&&send()} placeholder="Pergunte algo..." className="flex-1 bg-black/40 border border-white/10 rounded-full px-6 py-3 outline-none focus:border-purple-500"/>
                      <button onClick={()=>send()} disabled={busy} className="w-12 h-12 rounded-full bg-gradient-to-br from-[#8b5cf6] to-[#06b6d4] flex items-center justify-center">{busy?<Zap size={18} className="animate-spin"/>:<Send size={18}/>}</button>
                    </div>
                  </div>
                  <p className="mt-4 text-xs opacity-40">Flow AI v3.0 • {settings.model} NVIDIA</p>
                </div>
              )}
              
              {/* CHAT SCREEN */}
              {active==='chat' && (
                <div className="max-w-4xl mx-auto flex flex-col h-full">
                  <div className="space-y-3 flex-1 overflow-auto">
                    {messages.map((m,i)=><div key={i} className={`glass rounded-2xl p-4 ${m.role==='user'?'ml-12 border-cyan-500/30':'mr-12 border-purple-500/30'}`}>
                      <div className="flex justify-between"><span className={`text-xs font-bold ${m.role==='user'?'text-cyan-300':'text-purple-300'}`}>{m.role==='user'?'Você':'Flow'}</span><span className="text-[10px] opacity-40">{m.time}</span></div>
                      <p className="mt-1 text-sm opacity-90 whitespace-pre-wrap">{m.text}{m.streaming && <span className="animate-pulse text-purple-300"> ▌</span>}</p>
                      {m.role==='flow' && !m.streaming && extractBash(m.text).length>0 && !m.exec && (
                        <button onClick={()=>runCmd(extractBash(m.text)[0], i)} className="mt-2 text-xs bg-gradient-to-br from-[#8b5cf6]/40 to-[#06b6d4]/40 border border-purple-500/40 rounded-lg px-3 py-1.5 flex items-center gap-2"><Play size={12}/> Executar comando</button>
                      )}
                      {m.exec && <pre className="mt-2 text-[11px] bg-black/50 border border-white/10 rounded-xl p-3 overflow-auto max-h-56 whitespace-pre-wrap">{m.exec.stdout || m.exec.stderr || m.exec.error || JSON.stringify(m.exec)}</pre>}
                    </div>)}
                  </div>
                  <div className="flex gap-2 mt-3">
                    <button onClick={ouvir} className={`w-10 h-10 rounded-full flex items-center justify-center ${listening?'bg-red-500 animate-pulse':'bg-white/10 hover:bg-white/20'}`}><Mic size={18}/></button>
                    <input value={input} onChange={e=>setInput(e.target.value)} onKeyDown={e=>e.key==='Enter'&&send()} placeholder="Pergunte algo... (resposta aparece em tempo real)" className="flex-1 bg-black/40 border border-white/10 rounded-full px-5 py-2.5 outline-none focus:border-purple-500"/>
                    <button onClick={()=>send()} disabled={busy} className="w-10 h-10 rounded-full bg-gradient-to-br from-[#8b5cf6] to-[#06b6d4] flex items-center justify-center">{busy?<Zap size={16} className="animate-spin"/>:<Send size={16}/>}</button>
                  </div>
                </div>
              )}
              
              {/* AÇÃO (VER E AGIR) SCREEN */}
              {active==='acao' && (
                <div className="max-w-4xl mx-auto">
                  <h1 className="text-2xl font-bold mb-1 flex items-center gap-2"><Radar className="text-purple-400"/> Ver a tela e agir</h1>
                  <p className="text-sm opacity-60 mb-4">Peça em linguagem natural. Eu vejo a tela, monto o plano e executo (abrir site, clicar, digitar) via Playwright.</p>
                  <div className="glass rounded-2xl p-4 space-y-3">
                    <textarea value={acaoPrompt} onChange={e=>setAcaoPrompt(e.target.value)} rows={2} className="w-full bg-black/40 border border-white/10 rounded-xl px-4 py-3 outline-none focus:border-purple-500" placeholder="Ex: abra o YouTube e pesquise lofi para focar"/>
                    <div className="flex gap-2">
                      <button onClick={agir} disabled={acaoBusy} className="bg-gradient-to-br from-[#8b5cf6] to-[#06b6d4] px-6 py-2.5 rounded-xl font-semibold flex items-center gap-2"><Sparkles size={16}/> {acaoBusy?'Executando...':'Ver e Agir'}</button>
                      <input value={digTela} onChange={e=>setDigTela(e.target.value)} onKeyDown={e=>e.key==='Enter'&&digitarTela()} placeholder="Digitar texto na tela..." className="flex-1 bg-black/40 border border-white/10 rounded-xl px-4 py-2.5 outline-none focus:border-purple-500"/>
                      <button onClick={digitarTela} disabled={acaoBusy} className="bg-white/10 hover:bg-white/20 px-5 rounded-xl text-sm flex items-center gap-2"><Brain size={15}/> Digitar</button>
                    </div>
                  </div>
                  {acaoBusy && <div className="glass rounded-2xl p-6 mt-4 text-center opacity-70">🔍 Analisando a tela e montando o plano...</div>}
                  {acaoResult && (
<div className="glass rounded-2xl p-4 mt-4 space-y-3">
                       {acaoResult.error && <p className="text-red-300 text-sm">Erro: {acaoResult.error}</p>}
                       {acaoResult.passos && <div><h3 className="text-xs font-bold text-purple-300 mb-1">Passos executados</h3><div className="flex flex-wrap gap-2">{acaoResult.passos.map((p,i)=><span key={i} className="text-xs bg-purple-500/20 border border-purple-500/40 rounded-lg px-2 py-1">{p}</span>)}</div></div>}
                       {acaoResult.plano && (
                       <div>
                         <h3 className="text-xs font-bold text-cyan-300 mb-1">Plano vision</h3>
                         <pre className={`text-[11px] bg-black/50 border border-white/10 rounded-xl p-3 overflow-auto whitespace-pre-wrap`}>
                           {JSON.stringify(acaoResult.plano, null, 1)}
                         </pre>
                       </div>
                       )}
                       {acaoResult.resposta && <p className="text-sm opacity-90">{acaoResult.resposta}</p>}
                       {acaoResult.titulo && <p className="text-xs opacity-50">🧭 {acaoResult.titulo}</p>}
                     </div>
                  )}
                </div>
              )}
              
              {/* TIMERS SCREEN */}
              {active==='timers' && (
                <div className="max-w-3xl mx-auto">
                  <h1 className="text-2xl font-bold mb-1 flex items-center gap-2"><AlarmClock className="text-amber-400"/> Timers e Alarmes</h1>
                  <p className="text-sm opacity-60 mb-4">Crie timers com nome. Também dá pra pedir no chat: "timer 10 minutos macarrão" ou "me lembra de beber água daqui a 30 minutos".</p>
                  <div className="glass rounded-2xl p-4 mb-5 grid grid-cols-[1fr_130px_auto] gap-3">
                    <input value={timerForm.nome} onChange={e=>setTimerForm({...timerForm,nome:e.target.value})} onKeyDown={e=>e.key==='Enter'&&criarTimer()} placeholder='Nome (ex: ovo, macarrão, pausa)' className="bg-black/40 border border-white/10 rounded-xl px-4 py-2.5 outline-none focus:border-amber-500"/>
                    <div className="flex gap-2">
                      <input type="number" min="1" max="999" value={timerForm.min} onChange={e=>setTimerForm({...timerForm,min:Number(e.target.value)})} className="flex-1 w-20 bg-black/40 border border-white/10 rounded-xl px-3 py-2.5 outline-none focus:border-amber-500"/>
                      <span className="self-center text-xs opacity-50">min</span>
                    </div>
                    <button onClick={()=>criarTimer()} className="bg-gradient-to-br from-amber-500 to-orange-500 px-5 rounded-xl font-semibold flex items-center gap-2"><Plus size={16}/> Iniciar</button>
                    <div className="col-span-3 flex gap-2 flex-wrap">
                      {[1,3,5,10,25,60].map(m=><button key={m} onClick={()=>criarTimer(m+' min', m)} className="bg-white/10 hover:bg-white/20 rounded-xl px-4 py-1.5 text-sm">{m} min</button>)}
                      {timers.length===0 && <span className="text-xs opacity-50 self-center">Nenhum timer ativo.</span>}
                    </div>
                  </div>
                  <div className="grid gap-3">
                    {timers.map(t=>{const rest = Math.max(0, Math.round(t.fim - Date.now()/1000)); const mm=Math.floor(rest/60), ss=rest%60
                      return <div key={t.id} className="glass rounded-2xl p-4 flex items-center gap-4 border-amber-500/30">
                        <div className="text-3xl font-bold font-mono w-36 tabular-nums text-amber-300">{String(mm).padStart(2,'0')}:{String(ss).padStart(2,'0')}</div>
                        <div className="flex-1"><p className="font-semibold">{t.nome}</p><p className="text-xs opacity-50">{rest===0?'terminou!':('faltando '+mm+' min')}</p></div>
                        {rest===0 && <p className="text-amber-300 animate-pulse">🔔</p>}
                        <button onClick={()=>cancelTimer(t.id)} className="w-8 h-8 rounded-lg bg-red-500/20 flex items-center justify-center"><X size={15} className="text-red-400"/></button>
                      </div>})}
                    {timers.length===0 && <div className="glass rounded-2xl p-8 text-center opacity-50"><AlarmClock size={36} className="mx-auto mb-2 opacity-40"/><p>Sem timers ativos agora</p></div>}
                  </div>
                </div>
              )}
              
              {/* RECEITAS SCREEN */}
              {active==='receitas' && (
                <div className="max-w-4xl mx-auto">
                  <h1 className="text-2xl font-bold mb-1 flex items-center gap-2"><ChefHat className="text-rose-400"/> Receitas da Flow</h1>
                  <p className="text-sm opacity-60 mb-4">Busca em sites confiáveis e devolve apenas o link — crédito sempre do site original (nunca hospedamos o conteúdo).</p>
                  <div className="glass rounded-2xl p-4 mb-4">
                    <div className="flex gap-2">
                      <input value={receitaQuery} onChange={e=>setReceitaQuery(e.target.value)} onKeyDown={e=>e.key==='Enter'&&buscarReceitas()} placeholder='Ex: feijoada, bolo de cenoura, pudim...' className="flex-1 bg-black/40 border border-white/10 rounded-xl px-4 py-2.5 outline-none focus:border-rose-500"/>
                      <button onClick={buscarReceitas} disabled={receitaBusy} className="bg-gradient-to-br from-rose-500 to-orange-400 px-6 rounded-xl font-semibold flex items-center gap-2">{receitaBusy?<RotateCw size={16} className="animate-spin"/>:<ChefHat size={16}/>} {receitaBusy?'Buscando...':'Buscar'}</button>
                    </div>
                    <div className="flex gap-2 mt-3 flex-wrap">
                      <span className="text-xs opacity-50 self-center">Fontes:</span>
                      {['todos','TudoGostoso','Panelinha'].map(s=><button key={s} onClick={()=>setReceitaSite(s)} className={`text-xs rounded-lg px-3 py-1 ${receitaSite===s?'bg-rose-500/30 border border-rose-500/50':'bg-white/10 hover:bg-white/20 border border-transparent'}`}>{s}</button>)}
                    </div>
                  }
                  {receitaBusy && <div className="glass rounded-2xl p-8 text-center opacity-60"><RotateCw size={28} className="mx-auto mb-2 animate-spin"/><p>Flow está procurando nos sites de receita...</p></div>}
                  <div className="grid gap-3">
                    {receitas.map((r,i)=><div key={i} className="glass rounded-2xl p-4 flex items-center gap-3">
                      <div className="w-10 h-10 rounded-xl bg-rose-500/20 flex items-center justify-center shrink-0"><ChefHat size={18} className="text-rose-300"/></div>
                      <div className="flex-1 min-w-0"><p className="font-semibold truncate">{r.titulo}</p><p className="text-xs opacity-50">{r.site}</p></div>
<button onClick={()=>abrirReceita(r.url)} className="bg-white/10 hover:bg-white/20 rounded-xl px-4 py-2 text-sm flex items-center gap-2 shrink-0"><Link2 size={14}/> Abrir</button>
                       <a href={r.url} target="_blank" rel="noreferrer" className="text-xs text-cyan-400 underline shrink-0">ver no site</a>
                     </div>) }
                     {receitas.length===0 && !receitaBusy && <div className="glass rounded-2xl p-8 text-center opacity-50"><ChefHat size={36} className="mx-auto mb-2 opacity-40"/><p>Busque uma receita — a Flow traz os melhores links legítimos</p></div>}
                   </div>
                </div>
              )}
              
              {/* MÚSICA SCREEN */}
              {active==='musica' && (
                <div className="max-w-4xl mx-auto">
                  <h1 className="text-2xl font-bold mb-6 flex items-center gap-2"><Music className="text-cyan-400"/> Música</h1>
                  {agora && agora.players.length>0 && (
                    <div className="glass rounded-2xl p-5 mb-4 border-cyan-500/30">
                      <div className="flex items-center gap-4">
                        <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-purple-500 to-cyan-400 flex items-center justify-center">
                          {agora.status==='Playing'?<Play size={24} className="text-white"/>:<Square size={20} className="text-white"/>}
</div>
                         <div className="flex-1 min-w-0">
                           <p className="font-bold truncate">{agora.titulo}</p>
                           <p className="text-xs opacity-60 truncate">{agora.artista}</p>
                           <p className="text-[10px] opacity-40 mt-0.5 capitalize">{agora.status} • {agora.player.split('.').pop()}{agora.volume!=null?` • ${agora.volume}%`:''}</p>
                         </div>
                         <button onClick={()=>atualizaMusica()} className="bg-white/10 hover:bg-white/20 rounded-xl px-3 py-2 text-sm flex items-center gap-2"><RotateCw size={14}/> Atualizar</button>
                       </div>
                     )}
                    <div className="grid md:grid-cols-2 gap-4">
                      <div className="glass rounded-2xl p-5 space-y-4">
                        <h2 className="font-semibold text-sm opacity-80">Players detectados</h2>
                        {players.length===0 && <p className="text-xs opacity-50">Nenhum player de música aberto (abre o Spotify ou um player local pra eu controlar).</p>}
                        <div className="flex flex-wrap gap-2">
                          {players.map(p=><span key={p} className="text-xs bg-cyan-500/20 border border-cyan-500/40 rounded-lg px-2 py-1">{p.split('.')[1]}</span>)}
                        </div>
                        <div className="flex gap-2">
                          <button onClick={()=>musicaCmd('play')} className="flex-1 bg-white/10 hover:bg-white/20 rounded-xl py-2 font-semibold"><Play size={16} className="inline mr-1"/> Play</button>
                          <button onClick={()=>musicaCmd('pause')} className="flex-1 bg-white/10 hover:bg-white/20 rounded-xl py-2 font-semibold"><Square size={15} className="inline mr-1"/> Pausa</button>
                          <button onClick={()=>musicaCmd('next')} className="flex-1 bg-white/10 hover:bg-white/20 rounded-xl py-2 font-semibold">Próxima</button>
                          <button onClick={()=>musicaCmd('previous')} className="flex-1 bg-white/10 hover:bg-white/20 rounded-xl py-2 font-semibold">Anterior</button>
                        </div>
                        <div>
                          <label className="text-xs opacity-60">Volume: {volume}%</label>
                          <input type="range" min="0" max="100" value={volume} onChange={e=>{setVolume(Number(e.target.value))}} onMouseUp={e=>musicaCmd('volume',{volume:Number(e.target.value)})} className="w-full accent-cyan-400"/>
                        </div>
                      </div>
                      <div className="space-y-4">
                        <div className="glass rounded-2xl p-5">
                          <h2 className="font-semibold text-sm opacity-80 mb-3">Tocar no YouTube</h2>
                          <div className="flex gap-2">
                            <input value={musicaQuery} onChange={e=>setMusicaQuery(e.target.value)} onKeyDown={e=>e.key==='Enter'&&musicaCmd('tocar',{query:musicaQuery})} placeholder='Ex: lofi para focar' className="flex-1 bg-black/40 border border-white/10 rounded-xl px-4 py-2.5 outline-none focus:border-cyan-500"/>
                            <button onClick={()=>musicaCmd('tocar',{query:musicaQuery})} className="bg-gradient-to-br from-purple-500 to-cyan-400 px-5 rounded-xl font-semibold">Tocar</button>
                          </div>
                          <p className="text-[10px] opacity-40 mt-2">Abre o YouTube Music no navegador da Flow e dá play no primeiro resultado.</p>
                        </div>
                        <div className="glass rounded-2xl p-5">
                          <h2 className="font-semibold text-sm opacity-80 mb-3">Sons ambiente (royalty-free)</h2>
                          <div className="flex flex-wrap gap-2">
                            {sons.map(s=>{const n=s.split('.')[0]; return (<button key={s} onClick={()=>musicaCmd('tocar',{query:n})} className="bg-white/10 hover:bg-white/20 rounded-xl px-4 py-2 text-sm capitalize">{n}</button>);})}
                          </div>
                          <button onClick={()=>musicaCmd('parar_som')} className="bg-red-500/20 text-red-300 hover:bg-red-500/30 rounded-xl px-4 py-2 text-sm">Parar</button>
                          {sons.length===0 && <p className="text-xs opacity-50">Nenhum som ambiente disponível.</p>
                          }
                        </div>
                        <div className="glass rounded-2xl p-5">
                          <h2 className="font-semibold text-sm opacity-80 mb-3">Música local (pasta ~/Música)</h2>
                          <div className="flex gap-2 mb-3">
                            <input value={localQuery} onChange={e=>setLocalQuery(e.target.value)} onKeyDown={e=>e.key==='Enter'&&tocarLocal(localQuery)} placeholder="Nome do arquivo ou filtre..." className="flex-1 bg-black/40 border border-white/10 rounded-xl px-4 py-2 text-sm outline-none focus:border-cyan-500"/>
                            <button onClick={()=>tocarLocal(localQuery)} className="bg-white/10 hover:bg-white/20 rounded-xl px-4 text-sm"><Play size={14} className="inline mr-1"/>Tocar</button>
                          </div>
                          <div className="max-h-44 overflow-auto space-y-1">
                            {locais.filter(f=>!localQuery || f.toLowerCase().includes(localQuery.toLowerCase())).map(f=><button key={f} onClick={()=>tocarLocal(f)} className="w-full text-left text-xs bg-black/30 hover:bg-white/10 rounded-lg px-3 py-2 truncate">{f}</button>)}
                            {locais.length===0 && !localQuery && <p className="text-xs opacity-50">Pasta vazia. Coloque MP3 em <span className="font-mono">~/Música</span> ou me diga o caminho.</p>}
                          }
                        }
                      </div>
                    }
                  }
                  {musicaMsg && <div className="glass rounded-2xl p-4 mt-4 text-sm opacity-90">{musicaMsg}</div>}
                </div>
              )}
              
              {/* FOCO SCREEN */}
              {active==='foco' && (
                <div className="max-w-3xl mx-auto">
                  <h1 className="text-2xl font-bold mb-6 flex items-center gap-2"><Timer className="text-orange-400"/> Modo Foco</h1>
                  <div className="glass rounded-2xl p-6 space-y-5">
                    <div className="flex items-end gap-4">
                      <div>
                        <label className="text-xs opacity-60">Pomodoro (min)</label>
                        <input type="number" min="1" max="120" value={focoMin} onChange={e=>setFocoMin(Number(e.target.value))} className="mt-1 block w-32 bg-black/40 border border-white/10 rounded-xl px-4 py-2.5"/>
                      </div>
                      <button onClick={()=>focoCmd('ativar')} disabled={foco?.ativo} className="bg-gradient-to-br from-orange-500 to-red-500 px-6 py-2.5 rounded-xl font-semibold disabled:opacity-40">🔕 Ativar foco</button>
                      <button onClick={()=>focoCmd('desativar')} disabled={!foco?.ativo} className="bg-white/10 hover:bg-white/20 px-6 py-2.5 rounded-xl font-semibold disabled:opacity-30">🔔 Desativar</button>
                    </div>
                    <p className="text-xs opacity-60">Ao ativar: silencia notificações, volume 50%, fecha Discord/WhatsApp/Telegram e liga o pomodoro escolhido.</p>
                    {foco?.timer && <div className="glass rounded-xl p-4 text-center border-orange-500/40"><p className="text-3xl font-bold text-orange-300">{Math.floor(foco.timer.faltando/60)}:{String(foco.timer.faltando%60).padStart(2,'0')}</p><p className="text-xs opacity-50 mt-1">faltando</p></div>}
                  </div>
                </div>
              )}
              
              {/* INTEGRAÇÕES SCREEN */}
              {active==='integracoes' && (
                <div className="max-w-5xl mx-auto">
                  <h1 className="text-2xl font-bold mb-1 flex items-center gap-2"><CloudSun className="text-sky-400"/> Integrações</h1>
                  <p className="text-sm opacity-60 mb-4">Clima, sistema, lista de compras, notas, brilho e navegador (WhatsApp/Gmail/Calendário). Tudo também no chat/ voz: "como tá o clima?", "adiciona leite na lista".</p>
                  <div className="grid lg:grid-cols-2 gap-4">
                    <div className="glass rounded-2xl p-5">
                      <div className="flex items-center justify-between mb-3"><h2 className="font-semibold text-sm opacity-80 flex items-center gap-2"><CloudSun size={16} className="text-sky-400"/> Clima</h2>
                        <div className="flex gap-2">
                          <input value={climaCidade} onChange={e=>setClimaCidade(e.target.value)} onKeyDown={e=>e.key==='Enter'&&fetchClima()} placeholder="Cidade" className="w-28 bg-black/40 border border-white/10 rounded-lg px-3 py-1 text-sm outline-none focus:border-sky-500"/>
                          <button onClick={fetchClima} disabled={climaLoading} className="bg-gradient-to-br from-sky-500 to-indigo-500 rounded-lg px-3 py-1 text-sm font-semibold">{climaLoading?'...':'Buscar'}</button>
                        </div>
                      </div>
                      {clima?.ok ? (
                        <div>
                          <div className="flex items-center gap-4">
                            <div className="text-5xl font-light">{clima.atual.temp}°C</div>
                            <div><p className="font-semibold capitalize">{clima.atual.desc}</p>
                              <p className="text-xs opacity-60">sensação {clima.atual.sensacao}° • umidade {clima.atual.umidade}% • vento {clima.atual.vento}km/h</p>
                              <p className="text-[11px] opacity-50">máx {clima.hoje.max}° mín {clima.hoje.min}° • nascer {clima.hoje.nascer} pôr {clima.hoje.por}</p>
                            </div>
                          </div>
                          <div className="flex gap-2 mt-3 flex-wrap">
                            {clima.previsao.map((p,i)=>(<div key={i} className="bg-black/30 rounded-lg px-3 py-1.5 text-center flex-1"><p className="text-[10px] opacity-50">{p.dia.slice(5)}</p><p className="text-sm">{p.max}°/<span className="opacity-50">{p.min}°</span></p><p className="text-[10px] truncate">{p.desc}</p></div>))}
                          </div>
                        </div>
                        ) : clima?.error ? <p className="text-xs text-red-300">Erro: {clima.error} (precisa de internet)</p> : <p className="text-xs opacity-50">Busque o clima da sua cidade.</p>}
                      </div>
                      
                      <div className="glass rounded-2xl p-5">
                        <h2 className="font-semibold text-sm opacity-80 mb-3 flex items-center gap-2"><Gauge size={16} className="text-emerald-400"/> Sistema</h2>
{sysInfo ? (<div className="grid grid-cols-2 gap-2 text-xs">
                           <div className="bg-black/30 rounded-xl p-3"><p className="opacity-50 uppercase tracking-wide">Disco</p><p className="font-mono text-sm">{sysInfo.disco.uso_pct}</p><p className="opacity-50">{sysInfo.disco.livre} livre de {sysInfo.disco.total}</p></div>
                           <div className="bg-black/30 rounded-xl p-3"><p className="opacity-50 uppercase tracking-wide">RAM</p><p className="font-mono text-sm">{sysInfo.ram.usado} / {sysInfo.ram.total}</p><p className="opacity-50">{sysInfo.ram.disponivel} disponível</p></div>
                           <div className="bg-black/30 rounded-xl p-3"><p className="opacity-50 uppercase tracking-wide">CPU</p><p className="font-mono text-sm">{sysInfo.cpu.temp} • {sysInfo.cpu.nucleos} núcleos</p><p className="opacity-50">carga {sysInfo.cpu.load_1m}</p></div>
                           <div className="bg-black/30 rounded-xl p-3"><p className="opacity-50 uppercase tracking-wide">Uptime</p><p className="font-mono text-sm truncate">{sysInfo.uptime}</p></div>
                         </div>) : <p className="text-xs opacity-50">Carregando dados do sistema...</p>}
                        <div className="mt-4">
                          <div className="flex items-center justify-between"><label className="text-xs opacity-60">Brilho: {brilhoVal}%</label>
                            <button onClick={()=>setBrilho(100)} className="text-[10px] bg-white/10 rounded-lg px-2 py-1">100%</button></div>
                          <input type="range" min="1" max="100" value={brilhoVal} onChange={e=>setBrilho(Number(e.target.value))} className="w-full accent-emerald-400"/>
                          <div className="flex gap-2 mt-2">
                            <button onClick={abrirSite.bind(null,'whatsapp')} className="flex-1 bg-white/10 hover:bg-white/20 rounded-xl py-2 text-sm">WhatsApp Web</button>
                            <button onClick={abrirSite.bind(null,'gmail')} className="flex-1 bg-white/10 hover:bg-white/20 rounded-xl py-2 text-sm">Gmail</button>
                            <button onClick={abrirSite.bind(null,'calendario')} className="flex-1 bg-white/10 hover:bg-white/20 rounded-xl py-2 text-sm">Calendário</button>
                          </div>
                        </div>
                      </div>
                      
                      <div className="glass rounded-2xl p-5">
                        <h2 className="font-semibold text-sm opacity-80 mb-3 flex items-center gap-2"><ShoppingCart size={16} className="text-orange-400"/> Lista de Compras</h2>
                        <div className="flex gap-2 mb-3">
                          <input value={comprasItem} onChange={e=>setComprasItem(e.target.value)} onKeyDown={e=>e.key==='Enter'&&addCompra()} placeholder="Ex: leite, arroz, detergente..." className="flex-1 bg-black/40 border border-white/10 rounded-xl px-3 py-2 text-sm outline-none focus:border-orange-500"/>
                          <button onClick={addCompra} className="bg-orange-500/80 hover:bg-orange-500 rounded-xl px-4 text-sm font-semibold"><Plus size={15} className="inline mr-1"/>Add</button>
                        </div>
                        <div className="space-y-1 max-h-44 overflow-auto">
                          {compras.map((c,i)=><div key={i} className="flex items-center justify-between bg-black/30 rounded-lg px-3 py=2 text-sm">
                            <span className="truncate">{c.item} <span className="opacity-50">x{c.qtd}</span></span>
                            <button onClick={()=>delCompra(c.item)} className="w-6 h-6 rounded-md bg-red-500/20 flex items-center justify-center shrink-0"><X size={12} className="text-red-400"/></button>
                          </div>)}
                          {compras.length===0 && <p className="text-xs opacity-50">Lista vazia. Adicione no input ou no chat: "adiciona leite na lista".</p>}
                        </div>
                      </div>
                      
                      <div className="glass rounded-2xl p-5">
                        <h2 className="font-semibold text-sm opacity-80 mb-3 flex items-center gap-2"><NotebookPen size={16} className="text-cyan-400"/> Notas</h2>
                        <div className="flex gap-2 mb-3">
                          <input value={notaTexto} onChange={e=>setNotaTexto(e.target.value)} onKeyDown={e=>e.key==='Enter'&&addNota()} placeholder="Anote algo: pagar boleto, ligar pro dentista..." className="flex-1 bg-black/40 border border-white/10 rounded-xl px-3 py=2 text-sm outline-none focus:border-cyan-500"/>
                          <button onClick={addNota} className="bg-cyan-500/80 hover:bg-cyan-500 rounded-xl px-4 text-sm font-semibold"><Plus size={15} className="inline mr-1"/>Add</button>
                        </div>
                        <div className="space-y-1 max-h-44 overflow-auto">
                          {notas.map((n,i)=><div key={i} className="flex items-center justify-between gap-2 bg-black/30 rounded-lg px-3 py-2 text-sm">
                            <span className={`truncate ${n.feito?'line-through opacity-40':''}`}>#{n.id} {n.texto}</span>
                            {!n.feito && <button onClick={()=>delNota(n.id)} className="text-green-300 text-xs bg-green-500/20 rounded-lg px-2 py-1 shrink-0">feita ✓</button>}
                          </div>)}
                          {notas.length===0 && <p className="text-xs opacity-50">Nenhuma nota. Peça no chat: "anota pagar o boleto".</p>}
                        </div>
                      </div>
                    </div>
                  )}
                  
                  <div className="glass rounded-2xl p-5 mt-4">
                    <h2 className="font-semibold text-sm opacity-80 mb-3">WhatsApp</h2>
                    <div className="flex gap-2">
                      <input value={waDest} onChange={e=>setWaDest(e.target.value)} placeholder="Contato (ex: mamãe)" className="w-40 bg-black/40 border border-white/10 rounded-xl px-3 py=2 text-sm outline-none focus:border-green-500"/>
                      <input value={waMsg} onChange={e=>setWaMsg(e.target.value)} placeholder="Mensagem" className="flex-1 bg-black/40 border border-white/10 rounded-xl px-3 py=2 text-sm outline-none focus:border-green-500"/>
                      <button onClick={waEnviar} className="bg-green-500/80 hover:bg-green-500 rounded-xl px-4 text-sm font-semibold"><Plus size={15} className="inline mr-1"/>Enviar</button>
                    </div>
                  </div>
                </div>
              )}
              
              {/* ROTINAS SCREEN */}
              {active==='rotinas' && (
                <div className="max-w-4xl mx-auto">
                  <h1 className="text-2xl font-bold mb-1 flex items-center gap-2"><Wrench className="text-orange-400"/> Rotinas</h1>
                  <p className="text-sm opacity-60 mb-4">Rotinas são sequências de passos que podem ser executadas automaticamente ou sob demanda.</p>
                  <div className="glass rounded-2xl p-4 mb-4">
                    <div className="flex gap-2">
                      <input value={rotinaForm.nome} onChange={e=>setRotinaForm({...rotinaForm,nome:e.target.value})} placeholder="Nome da rotina" className="flex-1 bg-black/40 border border-white/10 rounded-xl px-4 py=2.5 outline-none focus:border-orange-500"/>
                      <button onClick={addPasso} className="bg-white/10 hover:bg-white/20 rounded-xl px-4 py=2 text-sm"><Plus size={14} className="inline mr-1" />Adicionar passo</button>
                    </div>
                    <div className="space-y-2">
                      {rotinaForm.passos.map((passo, index)=><div key={index} className="glass rounded-xl p-3 flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-orange-500/20 flex items-center justify-center"><Timer size={16} className="text-orange-300"/></div>
                        <div className="flex-1">
                          <div className="flex items-center gap-2">
                            <select value={passo.tipo} onChange={e=>setPasso(index,{...passo,tipo:e.target.value})} className="bg-black/30 border border-white/10 rounded-xl px-3 py=2">
                              <option value="notificacao">Notificação</option>
                              <option value="comando">Comando</option>
                              <option value="esperar">Esperar</option>
                              <option value="timer">Timer</option>
                              <option value="musica">Música</option>
                              <option value="clima">Clima</option>
                            </select>
                            <input value={passo.valor} onChange={e=>setPasso(index,{...passo,valor:e.target.value})} placeholder="Valor" className="flex-1 bg-black/40 border border-white/10 rounded-xl px-3 py=2">
                          </div>
                          <button onClick={()=>setPasso(index,{...passo,tipo:'remover'})} className="text-xs bg-red-500/20 rounded-lg px-2 py=1"Remover</button">
                        </div>
                      </div>)}
                    </div>
                    <div className="flex gap-2 mb-4">
                      <button onClick={criarRotina} className="bg-orange-500/80 hover:bg-orange-500 px-4 py=2 font-semibold"><Plus size={15} className="inline mr-1" />Criar Rotina</button">
                    </div>
                    {rotinaMsg && <div className="glass rounded-2xl p-4 text-sm opacity-90>{rotinaMsg}</div>}
                  </div>
                </div>
              )}
              
              {/* TASKS SCREEN */}
              {active==='tasks' && (
                <div className="max-w-4xl mx-auto">
                  <h1 className="text-2xl font-bold mb-1 flex items-center gap-2"><Calendar className="text-blue-400/> Tarefas Autônomas</h1">
                  <p className="text-sm opacity-60 mb-4>Tarefas que a Flow executa automaticamente em intervalos definidos.</p">
                  <div className="glass rounded-2xl p-4 mb-4">
                    <div className="flex gap-2">
                      <input value={taskForm.title} onChange={e=>setTaskForm({...taskForm,title:e.target.value})} placeholder="Título da tarefa" className="flex-1 bg-black/40 border border-white/10 rounded-xl px-4 py=2.5 outline-none focus:border-blue-500"/>
                      <input value={taskForm.command} onChange={e=>setTaskForm({...taskForm,command:e.target.value})} placeholder="Comando a executar" className="flex-1 bg-black/40 border border-white/10 rounded-xl px-4 py=2.5 outline-none focus:border-blue-500"/>
                      <div className="flex gap-2">
                        <input type="number" min="1" max="60" value={taskForm.intervalo} onChange={e=>setTaskForm({...taskForm,intervalo:Number(e.target.value)})} className="w-20 bg-black/40 border border-white/10 rounded-xl px-3 py=2.5 outline-none focus:border-blue-500"/>
                        <span className="self-center text-xs opacity-50>min</span">
                      </div>
                      <div className="flex gap-2">
                        <input type="time" value={taskForm.hora} onChange={e=>setTaskForm({...taskForm,hora:e.target.value})} className="bg-black/40 border border-white/10 rounded-xl px-3 py=2.5 outline-none focus:border-blue-500"/>
                        <span className="self-center text-xs opacity-50>hora</span">
                      </div>
                      <div className="flex items-center">
                        <label className="text-xs opacity-60>Ativa</label">
                        <input type="checkbox" checked={taskForm.active} onChange={e=>setTaskForm({...taskForm,active:e.target.checked})} className="h-4 w-4 text-blue-500/">
                      </div>
                    </div>
                    <button onClick={criarTask} className="bg-blue-500/80 hover:bg-blue-500 px-4 py=2 font-semibold"><Plus size={15} className="inline mr-1/>Criar Tarefa</button">
                  </div>
                  <div className="space-y-4">
                    {tasks.length>0 && (
                      <div className="space-y-2">
                        <h2 className="font-semibold text-sm opacity-80>Tarefas Ativas</h2">
                        <div className="space-y-1">
                          {tasks.map(t=><div key={t.id} className="glass rounded-2xl p-4 flex items-center gap-3">
                            <div className="w-10 h-10 rounded-xl bg-blue-500/20 flex items-center justify-center"><Calendar size={16} className="text-blue-300"/></div>
                            <div className="flex-1">
                              <p className="font-semibold>{t.title}</p">
                              <p className="text-xs opacity-50>{t.command}</p">
                              {p className="text-xs opacity-50>A cada {t.intervalo}min</p">
                            </div>
<div className="flex gap-2">
                              <button onClick={()=>toggleTask(t.id)} className="bg-white/10 hover:bg-white/20 rounded-xl px-3 py=2 text-sm>{t.active?'Pausar':'Ativar'}</button">
                              <button onClick={()=>runTask(t.id)} className="bg-white/10 hover:bg-white/20 rounded-xl px-3 py=2 text-sm>Executar Agora</button">
                              <button onClick={()=>delTask(t.id)} className="bg-red-500/20 text-red-300 hover:bg-red-500/30 rounded-xl px-3 py=2>Excluir</button">
                            </div>
                          </div>
                        )}
                      )}
                    {tasks.length===0 && <div className="glass rounded-2xl p-8 text-center opacity-50"><Calendar size={36} className="mx-auto mb-2 opacity-40/><p>Nenhuma tarefa criada ainda</p></div">}
                  </div>
                </div>
              )}
              
              {/* VISÃO SCREEN */}
              {active==='vision' && (
                <div className="max-w-4xl mx-auto">
                  <h1 className="text-2xl font-bold mb-1 flex items-center gap-2"><Eye className="text-blue-400/> Visão</h1">
                  <p className="text-sm opacity-60 mb-4>Peça para a Flow descrever o que vê na tela ou executar ações baseadas na visão.</p">
                  <div className="glass rounded-2xl p-4 mb-4">
                    <div className="flex gap-2">
                      <input value={visionPergunta} onChange={e=>setVisionPergunta(e.target.value)} onKeyDown={e=>e.key==='Enter'&&abrirVisao()} placeholder='Descreva tudo que você vê na tela e quais aplicações estão abertas' className="flex-1 bg-black/40 border border-white/10 rounded-xl px-4 py=2.5 outline-none focus:border-blue-500"/>
                      <button onClick={abrirVisao} className="bg-gradient-to-br from-blue-500 to-indigo-500 px-6 rounded-xl font-semibold>Analisar Tela</button">
                    </div>
                  </div>
                  {visionData && (
                    <div className="glass rounded-2xl p-4 mt-4">
                      {visionData.error && <p className="text-red-300 text-sm>Erro: {visionData.error}</p">}
                      {visionData.imagem && <img src={visionData.imagem} className="w-full rounded-xl border border-white/10 mb-4 max-h-[60vh] object-contain bg-black"/>}
                      {visionData.texto && <p className="text-sm opacity-90>{visionData.texto}</p">}
                    </div>
                  )}
                </div>
              )}
              
              {/* MEMÓRIA SCREEN */}
              {active==='memory' && (
                <div className="max-w-4xl mx-auto">
                  <h1 className="text-2xl font-bold mb-1 flex items-center gap-2"><Brain className="text-indigo-400/> Memória</h1">
                  <p className="text-sm opacity-60 mb-4>Armazene informações importantes para que a Flow possa lembrar e usar posteriormente.</p">
                  <div className="glass rounded-2xl p-4 mb-4">
                    <div className="flex gap-2">
                      <input value={memTexto} onChange={e=>setMemTexto(e.target.value)} onKeyDown={e=>e.key==='Enter'&&memAprender()} placeholder="O que você quer que eu lembre?" className="flex-1 bg-black/40 border border-white/10 rounded-xl px-4 py=2.5 outline-none focus:border-indigo-500"/>
                      <button onClick={memAprender} className="bg-gradient-to-br from-indigo-500 to-purple-500 px-6 rounded-xl font-semibold>Aprender</button">
                    </div>
                    <div className="flex gap-2 mt-4">
                      <input value={memBusca} onChange={e=>setMemBusca(e.target.value)} onKeyDown={e=>e.key==='Enter'&&memBuscar()} placeholder="O que você quer que eu lembre?" className="flex-1 bg-black/40 border border-white/10 rounded-xl px-4 py=2.5 outline-none focus:border-indigo-500"/>
                      <button onClick={memBuscar} className="bg-white/10 hover:bg-white/20 rounded-xl px-4 py=2 text-sm>Buscar</button">
                    </div>
                  </div>
                  {memRes && (
                    <div className="glass rounded-2xl p-4 mt-4">
                      {memRes.learned && <p className="text-green-300>{memRes.msg}</p">}
                      {memRes.results && <div className="space-y-2">
                        <h3 className="font-semibold text-sm opacity-80>Resultados</h3">
                        {memRes.results.map((r,i)=><div key={i} className="glass rounded-2xl p-3">
                          <p className="font-semibold">#{r.id}</p>
                          {p className="text-sm opacity-90>{r.texto}</p">
                          {p className="text-xs opacity-50>Criado: {r.criado}</p">
                        </div>)}
                      </div>
                    )}
                  )}
                </div>
              )}
              
              {/* CONFIGURAÇÕES SCREEN */}
              {active==='settings' && (
                <div className="max-w-3xl mx-auto">
                  <h1 className="text-2xl font-bold mb-1 flex items-center gap-2"><Settings className="text-indigo-400/> Configurações</h1">
                  <div className="glass rounded-2xl p-6 space-y-4">
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 rounded-xl bg-indigo-500/20 flex items-center justify-center"><Settings size={20} className="text-indigo-300"/></div>
                      <div className="flex-1">
                        <p className="font-semibold>Modelo de IA</p">
                        <div className="flex gap-2">
                          <label className="text-xs opacity-60>{settings.model}</label">
                          <select value={settings.model} onChange={e=>setSettings({...settings,model:e.target.value})} className="w-24 bg-black/40 border border-white/10 rounded-xl px-3 py=2">
                            <option value="strong">Strong (Padrão)</option>
                            <option value="balanced">Balanced</option>
                            <option value="fast">Fast</option>
                          </select>
                        </div>
                        <p className="text-xs opacity-60 mt-1>Selecione o modelo de IA que a Flow deve usar para processar suas solicitações.</p">
                      </div>
                    </div>
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 rounded-xl bg-indigo-500/20 flex items-center justify-center"><Zap size={20} className="text-indigo-300"/></div>
                      <div className="flex-1">
                        <p className="font-semibold>Autonomia</p">
                        <div className="flex gap-2">
                          <label className="text-xs opacity-60>{settings.autonomy?'Ativada':'Desativada'}</label">
                          <input type="checkbox" checked={settings.autonomy} onChange={e=>setSettings({...settings,autonomy:e.target.checked})} className="h-4 w-4/">
                        </div>
                        <p className="text-xs opacity-60 mt-1>Quando ativada, a Flow pode tomar iniciativas e executar ações sem pedir confirmação explícita para tarefas rotineiras.</p">
                      </div>
                    </div>
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 rounded-xl bg-indigo-500/20 flex items-center justify-center"><Brain size={20} className="text-indigo-300"/></div>
                      <div className="flex-1">
                        <p className="font-semibold>Salvar configurações</p">
                        <button onClick={salvarSettings} className="bg-white/10 hover:bg-white/20 rounded-xl px-4 py=2 text-sm>Salvar</button">
                      </div>
                    </div>
                  </div>
                </div>
              )}
              
              {/* LOGS SCREEN */}
              {active==='logs' && (
                <div className="max-w-4xl mx-auto">
                  <h1 className="text-2xl font-bold mb-1 flex items-center gap-2"><Terminal className="text-gray-400/> Logs</h1">
                  <p className="text-sm opacity-60 mb-4>Logs de atividades da Flow para depuração e monitoramento.</p">
                  <div className="glass rounded-2xl p-6">
                    {logs.length>0 && (
                      <div className="space-y-2">
                        {logs.map((l,i)=><div key={i} className="glass rounded-xl p-3 flex items-center gap-3">
                          <div className="w-10 h-10 rounded-xl bg-gray-500/20 flex items-center justify-center"><Terminal size={16} className="text-gray-300"/></div>
                          <div className="flex-1">
                            <p className="font-semibold>{l.source}</p">
                            <p className="text-xs opacity-50">{l.message}</p>
                            <p className="text-xs opacity-50">{l.time}</p>
                          </div>
                        </div>)}
                    )}
                    {logs.length===0 && <div className="glass rounded-2xl p-8 text-center opacity-50"><Terminal size={36} className="mx-auto mb-2 opacity-40"/><p>Nenhum log disponível</p></div>}
                  </div>
                </div>
              )}
            </div>
          </div>
        </>
      )}
    </div>
  );
}
