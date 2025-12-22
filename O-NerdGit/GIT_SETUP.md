# Git Setup - O Nerd

## 🚀 Prepare seu projeto para GitHub em 5 minutos

### ✅ Pré-requisitos
- [Git instalado](https://git-scm.com/download/win)
- [Conta GitHub criada](https://github.com/signup)

---

## 📋 Passos (Execute em Ordem)

### 1️⃣ Abra o PowerShell no seu projeto
```powershell
cd "C:\Users\Anatalia\Downloads\O Nerd"
```

### 2️⃣ Configure seu Git (primeira vez apenas)
```powershell
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

### 3️⃣ Inicializa repositório local
```powershell
git init
git add .
git commit -m "Initial commit: O Nerd v2.0 Professional Edition"
```

### 4️⃣ Crie repositório no GitHub
1. Vá para https://github.com/new
2. Nome: `O-Nerd` (ou escolha outro)
3. Descrição: `Assistente de IA para Windows com suporte a voz`
4. Escolha **Public** ou **Private**
5. **NÃO** inicialize com README/LICENSE/.gitignore
6. Clique "Create repository"

### 5️⃣ Conecte ao GitHub (ESCOLHA UMA OPÇÃO)

#### Opção A: HTTPS (Mais fácil - Recomendado)
```powershell
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/O-Nerd.git
git push -u origin main
```

#### Opção B: SSH (Mais seguro)
```powershell
git branch -M main
git remote add origin git@github.com:SEU_USUARIO/O-Nerd.git
git push -u origin main
```

---

## 🔑 Substitua SEU_USUARIO!

Seu username do GitHub é a parte antes do `/` em `github.com/SEU_USUARIO`

**Exemplo:**
```
github.com/anatalia         → SEU_USUARIO = "anatalia"
https://github.com/anatalia/O-Nerd
```

---

## ✨ Pronto! Seu código está no GitHub

Agora você pode:
- ✅ Clonar em outro PC: `git clone https://github.com/SEU_USUARIO/O-Nerd.git`
- ✅ Compartilhar com amigos
- ✅ Fazer contribuições
- ✅ Rastrear mudanças

---

## 📝 Próximas Operações (Git Básico)

### Ver status
```powershell
git status
```

### Adicionar mudanças
```powershell
git add .                    # Todos os arquivos
git add arquivo.py           # Arquivo específico
```

### Fazer commit
```powershell
git commit -m "fix: corrigir erro no reconhecimento de voz"
git commit -m "feat: adicionar novo comando"
git commit -m "docs: atualizar README"
```

### Fazer push (enviar para GitHub)
```powershell
git push
git push origin main  # Alternativa
```

### Ver histórico
```powershell
git log                      # Ver commits
git log --oneline           # Resumido
```

---

## 🆘 Resolvendo Problemas

### Erro: "fatal: not a git repository"
**Solução:** Você não está na pasta correta
```powershell
cd "C:\Users\Anatalia\Downloads\O Nerd"
pwd  # Confirma que está no lugar certo
```

### Erro: "git: The term 'git' is not recognized"
**Solução:** Git não está instalado
1. Baixe https://git-scm.com/download/win
2. Execute instalador
3. Reinicie PowerShell
4. Teste com `git --version`

### Erro: "fatal: remote origin already exists"
**Solução:** Já existe um remote
```powershell
git remote -v                           # Ver remotes
git remote remove origin                # Remover
git remote add origin https://...       # Adicionar novamente
```

### Erro: "fatal: src refspec main does not match any"
**Solução:** Não há commits
```powershell
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

### Erro: Authentication failed
**Solução para HTTPS:**
1. GitHub pedirá seu token (não a senha)
2. Gere em https://github.com/settings/tokens
3. Cole quando pedido

**Solução para SSH:**
1. Gere chave: `ssh-keygen -t ed25519`
2. Adicione em https://github.com/settings/keys
3. Teste com `ssh -T git@github.com`

---

## 🔄 Fluxo de Trabalho Diário

```powershell
# 1. Ver o que mudou
git status

# 2. Adicionar mudanças
git add .

# 3. Fazer commit com mensagem descritiva
git commit -m "feat: descrição do que foi feito"

# 4. Enviar para GitHub
git push
```

---

## 📚 Comandos Essenciais Rápidos

| Comando | O que faz |
|---------|-----------|
| `git init` | Inicializa novo repositório |
| `git add .` | Adiciona todos os arquivos |
| `git commit -m "msg"` | Salva snapshot do código |
| `git push` | Envia para GitHub |
| `git pull` | Baixa mudanças do GitHub |
| `git status` | Mostra arquivos mudados |
| `git log` | Mostra histórico |
| `git branch` | Lista branches |
| `git checkout -b nome` | Cria nova branch |

---

## 🎯 Primeiro PR (Opcional)

Se quiser fazer sua primeira contribuição:

```powershell
# 1. Faça um fork no GitHub (botão no topo)
# 2. Clone seu fork
git clone https://github.com/SEU_USUARIO/O-Nerd.git

# 3. Crie uma branch
git checkout -b feature/minha-feature

# 4. Faça mudanças e commit
git add .
git commit -m "feat: sua feature"

# 5. Push para seu fork
git push origin feature/minha-feature

# 6. Abra um Pull Request no GitHub
```

---

## 🎓 Próximos Passos

Depois de colocar no GitHub:

1. **Adicione colaboradores:**
   - Settings → Collaborators → Add people

2. **Configure branch protection:**
   - Settings → Branches → Require pull requests

3. **Ative Actions:**
   - Criar testes automáticos
   - Verificar código automaticamente

4. **Crie Issues:**
   - Rastreie bugs e features

5. **Crie Releases:**
   - Versione seu código: v1.0, v2.0, etc

---

## 💡 Dicas Pro

✅ **Commits descritivos**
```
✓ git commit -m "feat: adicionar comando de volume"
✗ git commit -m "fix"
```

✅ **Faça commits frequentes**
```
✓ Muitos commits pequenos
✗ Um commit gigante
```

✅ **Use mensagens claras**
```
feat: feature nova
fix: correção de bug
refactor: reorganizar código
docs: documentação
test: testes
```

✅ **Sempre pull antes de push**
```powershell
git pull
git push
```

---

## 📖 Referências

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

<div align="center">

**Seu projeto está pronto para o mundo! 🌍**

Agora é oficial. Compartilhe com seus colegas! 🚀

</div>
