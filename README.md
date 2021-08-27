## Назначение проекта:

построеине безопасности в цикле CI/CD

## Технические детали
- pipeline предназначен для работы с Gitlab CI
- поддерживает и поставляется вместе со следующими тулами:
  - gitleaks
  - trufflehog
  - dependency check
  - gosec
  - phpcs
  - semgrep



## Чеклист на внедрение и доробку в своем контуре
1. Склонировать к себе common security pipeline
2. Исправить все места где встречается комментарий CHECK IT или FIX IT
3. Изменить в ./pipeline/security_tools.yml путь в registry до контейнеров в соотвествии с тем где вы их храните
4. Поднять у себя DefectDojo (см. https://github.com/DefectDojo/django-DefectDojo/blob/master/DOCKER.md)
5. Прописать у себя API-ключ, путь до DefectDojo для доступа к вашему DefectDojo в файле ./dd_prepare/dd_prepare.py. Если у вас используется Vault или аналогичное решение, то дороботать код проекта для получения API в runtime самостоятельно


## О тулах
мы не поставляем вместе с проектом исходники контейеров с security-тулами. Вам необходимо сбилдить и положить в регистре самостоятельно с учетом ваших политик безопасности. Так же важно добавить во все контейнеры следующие пакеты:
- openssh - ssh-клиент, нужен чтобы в некоторых случаях выполнять дополнительное клонирвоание проектов
- curl - для отправки данных в DefectDojo
- jq - для красивого отображания получаемого в ответ json


### назначение ./dd_prepare 
1. creates a project, engagement in DD
2. define variables

### назначение ./pipeline
directory with main pipeline
1. Run docker with dd_prepare
2. Run security tools
3. upload results to DD

### назначение.gitlab-ci.yml
1. build
2. test


# TODO:
- генерация пайплайна в рантайме на основе шаблонов jinja2
- добавление security-тулов

## Участники проекта:
- @httpnotonly - дал много полезной информации на старте
- https://t.me/true_hero - реализация ранних версий пайплайна
- @edgesecc (telegram: @edgesec) - стратегическое сопровождение, полный рефакторинг, вывод в паблик
- https://t.me/BlackDiver - здоровая критика


# реализация на инфраструктуре gitlab
Просто смотреть исходник на github не очень интересно. Лучше смотреть на работающие пайплайны
https://gitlab.com/common_security_pipeline/common_security_pipeline


## доп материалы:
презентация: https://docs.google.com/presentation/d/11h8trTpEXv35gEjP2mbRB7DK2J4PTpk_lzWMtwK9l5E/edit#slide=id.p8

