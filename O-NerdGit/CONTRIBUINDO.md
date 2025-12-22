# Contribuindo para O Nerd

Obrigado por considerar contribuir com o O Nerd! Este documento fornece diretrizes para reportar bugs e enviar melhorias.

## 📋 Código de Conduta

Seja respeitoso com os outros contribuidores. Rejeitaremos contribuições que contenham abuso ou assédio.

## 🐛 Reportando Bugs

Antes de criar um report de bug:
- Verifique se o bug já foi reportado em Issues
- Tente reproduzir em uma instalação limpa
- Reúna informações de diagnóstico

Ao criar um bug report, inclua:
- Seu SO e versão
- Versão do Python
- Passos exatos para reproduzir
- Comportamento observado
- Comportamento esperado
- Screenshots (se aplicável)

### Exemplo de Bug Report
```
Título: Erro de conexão com microfone em Windows 11

## Descrição
O microfone não é detectado ao executar `python start.py`

## Para Reproduzir
1. Execute `python start.py`
2. Digite "modo voz"
3. Fale algo

## Comportamento Observado
Erro: "Microfone não disponível"

## Informações
- OS: Windows 11 Pro
- Python: 3.11.5
- Microfone: USB Logitech
```

## 💡 Sugerindo Melhorias

Antes de sugerir uma melhoria:
- Verifique se já não foi sugerida
- Seja claro sobre o caso de uso

### Exemplo de Sugestão
```
Título: Suporte a múltiplos idiomas

## Descrição
Adicionar suporte para português europeu, inglês e espanhol

## Justificativa
Usuários em outros países poderiam usar a ferramenta

## Implementação Possível
Adicionar seleção de idioma em config.py
```

## 🔧 Processo de Contribuição

### 1. Faça um Fork
```bash
git clone https://github.com/seu-usuario/O-Nerd.git
cd O-Nerd
```

### 2. Crie uma Branch
```bash
git checkout -b feature/sua-feature
```

Padrão de nome:
- `feature/nova-funcionalidade` - para novas features
- `fix/corrigir-bug` - para correções
- `refactor/melhorar-codigo` - para refatoração
- `docs/atualizar-documentacao` - para docs

### 3. Faça Suas Mudanças
- Siga o guia de estilo em DESENVOLVIMENTO.md
- Escreva testes para novas funcionalidades
- Atualize documentação conforme necessário
- Use commits descritivos

### 4. Teste Localmente
```bash
# Formatação
black .

# Linting
pylint *.py

# Type checking
mypy *.py

# Testes
pytest
```

### 5. Faça um Commit
```bash
git add .
git commit -m "feat: descrição clara da mudança"
```

### 6. Faça um Push
```bash
git push origin feature/sua-feature
```

### 7. Abra um Pull Request
- Descreva suas mudanças
- Referencie qualquer issue relacionada (#123)
- Inclua screenshots se aplicável

### Checklist do PR
- [ ] Seguiu o guia de estilo
- [ ] Adicionou testes (se aplicável)
- [ ] Atualizou documentação
- [ ] Verificou com Black/Pylint/Mypy
- [ ] Todos os testes passam
- [ ] Sem quebra de funcionalidades existentes

## 📝 Padrão de Commit

Siga o Conventional Commits:

```
<tipo>(<escopo>): <descrição>

<corpo>

<rodapé>
```

### Tipos
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `refactor`: Reorganização de código
- `perf`: Melhoria de performance
- `test`: Adição/modificação de testes
- `docs`: Atualização de documentação
- `chore`: Outras mudanças (deps, config)

### Exemplos
```
feat(commands): adicionar comando para ajustar brightness

fix(voice): corrigir detecção de microfone em Windows 11

docs(readme): melhorar instruções de instalação

refactor(config): simplificar estrutura de constantes
```

## 🎯 Diretrizes de Código

### Style Guide
- Siga PEP 8
- Use Black para formatação
- Limite de 100 caracteres por linha

### Type Hints
```python
# ✓ CORRETO
def processar(entrada: str, contador: int) -> Dict[str, int]:
    pass

# ✗ ERRADO
def processar(entrada, contador):
    pass
```

### Docstrings
```python
# ✓ CORRETO
def minha_funcao(param: str) -> str:
    """Descrição breve.
    
    Descrição mais longa se necessário.
    
    Args:
        param: Descrição do parâmetro
        
    Returns:
        Descrição do retorno
    """
    pass

# ✗ ERRADO
def minha_funcao(param):
    # função importante
    pass
```

### Tratamento de Erros
```python
# ✓ CORRETO
try:
    resultado = operacao()
except ValueError as error:
    logger.error(f"Valor inválido: {error}")
    
# ✗ ERRADO
try:
    resultado = operacao()
except:
    pass
```

## 🧪 Testes

Toda nova funcionalidade deve ter testes:

```python
# test_novo_comando.py
import pytest
from commands import meu_novo_comando

def test_meu_novo_comando():
    """Testa meu novo comando."""
    resultado = meu_novo_comando("teste")
    assert resultado is not None
    assert "sucesso" in resultado.lower()

def test_meu_novo_comando_erro():
    """Testa tratamento de erro."""
    with pytest.raises(ValueError):
        meu_novo_comando("")
```

Execute testes:
```bash
pytest
pytest -v  # Verbose
pytest --cov  # Com cobertura
```

## 📚 Documentação

Atualize a documentação para mudanças:

1. **README.md** - Instruções do usuário
2. **DESENVOLVIMENTO.md** - Guia de desenvolvimento
3. **Docstrings** - Documentação inline
4. **Comments** - Explicações de código complexo

## ✅ Checklist Final

Antes de fazer um PR:
- [ ] Código segue PEP 8
- [ ] Testes passam (100% cobertura em novo código)
- [ ] Documentação atualizada
- [ ] Sem código comentado deixado para trás
- [ ] Sem `print()` ou `import pdb` em produção
- [ ] Commits são claros e descritivos
- [ ] Nenhuma quebra de API existente

## 🎓 Aprendendo

Novidade no projeto? Comece por:
1. Leia [README.md](README.md)
2. Explore [DESENVOLVIMENTO.md](DESENVOLVIMENTO.md)
3. Olhe issues marcadas como `good-first-issue`
4. Abra uma issue perguntando como começar

## 📞 Dúvidas?

- Abra uma [Discussion](https://github.com/seu-usuario/O-Nerd/discussions)
- Comente em uma [Issue](https://github.com/seu-usuario/O-Nerd/issues)
- Envie um email para seu-email@example.com

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma Licença MIT do projeto.

---

**Obrigado por contribuir! 🙏**
