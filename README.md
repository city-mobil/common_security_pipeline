# Common Security Pipeline
## Описание проекта:
Данный проект является вариантом реализации DevSecOps практик, на базе:
- GitLab
- [DefectDojo](https://github.com/DefectDojo/django-DefectDojo/)
- OpenSouce tools
  - [gitleaks](https://github.com/zricethezav/gitleaks)
  - [trufflehog](https://github.com/trufflesecurity/truffleHog)
  - [dependency check](https://github.com/jeremylong/DependencyCheck)
  - [gosec](https://github.com/securego/gosec)
  - [phpcs](https://github.com/FloeDesignTechnologies/phpcs-security-audit)
  - [semgrep](https://github.com/returntocorp/semgrep)

Используйте данный репозиторий чтобы построить безопасность в цикле CI/CD.

## Quick Start
1. Склонировать к себе Common Security Pipeline
2. Исправить все места где встречается комментарий `CHECK IT` или `FIX IT`
3. Изменить в `./pipeline/security_tools.yml` путь до контейнеров с Security Tools
4. Поднять у себя [DefectDojo](https://github.com/DefectDojo/django-DefectDojo/blob/master/DOCKER.md)
5. Прописать у себя в GitLab необходимые переменные:
  - API-ключ
  - Путь до DefectDojo для доступа к вашему DefectDojo в файле `./dd_prepare/dd_prepare.py`.
  - Если у вас используется Vault или аналогичное решение, то дороботать код проекта для получения API в runtime самостоятельно

## Security Tools
Мы не поставляем вместе с проектом исходники контейеров с security-тулами. Вам необходимо сбилдить и положить в регистре самостоятельно с учетом ваших политик безопасности. Так же важно добавить во все контейнеры следующие пакеты:
- openssh - ssh-клиент, нужен чтобы в некоторых случаях выполнять дополнительное клонирование проектов
- curl - для отправки данных в DefectDojo
- jq - для красивого отображания получаемого в ответ json

## Пример реализации на инфраструктуре gitlab
Просто смотреть исходник на github не очень интересно. Лучше смотреть на [работающие пайплайны](https://gitlab.com/common_security_pipeline/common_security_pipeline).

## TODO:
- генерация пайплайна в рантайме на основе шаблонов jinja2
- добавление security-тулов

## Доп. материалы:
Презентация [ZeroNights2021](https://docs.google.com/presentation/d/11h8trTpEXv35gEjP2mbRB7DK2J4PTpk_lzWMtwK9l5E/edit#slide=id.p8)

## Участники проекта:
- [Максим Мошаров](https://www.linkedin.com/in/maxim-mosharov-50904113b/) - дал много полезной информации на старте
- [Александр Вознесенский](https://www.linkedin.com/in/voznesensky/) - реализация ранних версий пайплайна
- [Вацлав Довнар](https://www.linkedin.com/in/vatclav-dovnar/) - стратегическое сопровождение, полный рефакторинг, вывод в паблик
- [Георгий Старостин](https://www.linkedin.com/in/georgii-starostin-06932942/) - здоровая критика

## Спонсор проекта
![](static/img/city.logo.png)

## Лицензия
Common Security Pipeline лицензируется под [Apache License 2.0](LICENSE)
