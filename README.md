# may-claude-skills

Skills pessoais para o Claude Code. Cada pasta na raiz é uma skill (`<nome>/SKILL.md`).

| Skill | Para que serve |
|---|---|
| [`store-screenshots`](store-screenshots/SKILL.md) | Cria as artes de screenshots da App Store e do Google Play num canvas do Claude Design, com prints reais, dados de demonstração e um padrão fixo de layout. |

## Instalar num computador novo

```bash
git clone https://github.com/steevedevops/may-claude-skills.git ~/may-claude-skills
mkdir -p ~/.claude/skills
ln -s ~/may-claude-skills/store-screenshots ~/.claude/skills/store-screenshots
```

Com o link simbólico, um `git pull` em `~/may-claude-skills` atualiza a skill.
Sem link, copie a pasta: `cp -R ~/may-claude-skills/store-screenshots ~/.claude/skills/`.

Para usar só num projeto, coloque a pasta em `<projeto>/.claude/skills/`.

## Usar

No Claude Code, peça normalmente ("cria os screenshots da loja para o app X") ou chame
direto com `/store-screenshots`.
