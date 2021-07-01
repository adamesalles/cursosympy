# Como trabalhar na produção da apostila

## Requisitos

Ter o `jupyter-book` e o `ghp-import` também. Ambos são instaláveis pelo `pip`.

## Como fazer o deploy

```bash
jb build --all .
git add .
git commit -m 'mensagem'
git push
ghp-import -n -p -f _build/html
```