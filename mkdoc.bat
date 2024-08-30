chcp 65001

python -m litedoc mbcp -o docs/zh/api -l zh-Hans -f editLink=false  -cd class -fd def -md def -vd var -cs
python -m litedoc mbcp -o docs/en/api -l en -f editLink=false       -cd class -fd def -md def -vd var -cs
python -m litedoc mbcp -o docs/ja/api -l ja -f editLink=false       -cd class -fd def -md def -vd var -cs
python -m litedoc mbcp -o docs/zht/api -l zh-Hant -f editLink=false -cd class -fd def -md def -vd var -cs
