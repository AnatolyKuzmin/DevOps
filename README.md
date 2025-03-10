# DevOps 
это культура, методология и набор практик, направленных на улучшение взаимодействий между разработчиками (Development) и специалистами по эксплуатации (Operations). Основаная цель DevOps - ускорить выпуск качественного программного обеспечения.

### Основные принципы DevOps:
- **Культура сотрудничества:** DevOps способствует тесному взаимодействию между командами разработки и эксплуатации.
- **Автоматизация:** автоматизация процессов сборки, тестирования и развертывания.
- **Непрерывная интеграция и доставка (CI/CD):** регулярное и автоматизированное тестирование и развертывание кода.
- **Мониторинг и обратная связь:** постоянное отслеживание работы приложения и быстрая реакция на проблемы.
- **Инфраструктура как код (IaC):** управление инфраструктурой с помощью кода, что позволяет автоматизировать её создание и настройку.

### Основные практики DevOps:
- **Непрерывная интеграция (CI):** разработчики часто объединяют свой код в общий репозиторий, где автоматически запускаются тесты.
- **Непрерывная доставка (CD):** автоматическое развертывание кода в тестовые и производственные среды.
- **Инфраструктура как код (IaC):** использование инструментов, таких как Terraform и Ansible, для автоматизации управления инфраструктурой.
- **Мониторинг и логирование:** использование инструментов, таких как Prometheus, Grafana и ELK Stack, для отслеживания состояния приложений и инфраструктуры.
- **Микросервисы:** разбиение приложения на небольшие независимые сервисы, которые могут разрабатываться и развертываться отдельно.

### SDLC - Software Development Life Cycle
Жизненый цикл разработки ПО - это процесс создания, поддержки и обнолвения ПО.
- Сбор и анализ требований
- Проектирование
- Реализация
- Тестирование
- Развертывание
- Эксплуатация и поддержка
- Вывод в эксплуатацию

#### Модели разработки ПО
Водопадная модель(линейный подход), Agile(спринтами), DevOps

## Docker
это платформа для разработки, доставки, и запуска приложений в контейнерах.
### Основные концепции Docker
- **Контейнер:** Легковесный, изолированный процесс, который включает в себя приложение и все его зависимости.
- **Образ:** Шаблон для создания контейнеров. Образы содержат все необходимые файлы и настройки для запуска приложения.
- **Dockerfile:** Текстовый файл с инструкциями по созданию образа.<br>

**Пример запуска контейнера**<br>
```docker run -d -p 80:80 --name webserver nginx```
- -d — запускает контейнер в фоновом режиме.
- -p 80:80 — пробрасывает порт 80 вашего хоста на порт 80 контейнера.
- --name webserver — задает имя контейнера.
- nginx — имя образа, который будет использован (в данном случае это образ веб-сервера Nginx).

**Docker образ**  - это статичный файл, который содержит все необходимые компоненты для запуска приложения(код приложения, библиотеки и зависимости, инструкции для выполнения приложения)
**Dockerfile** - это текстовый файл, содержащий набор инструкций для сборки образа.
Основные команды:
1. FROM: базовый образ на основе которого будет создан образ
2. WORKDIR: устанавливает рабочую директорию для последующих инструкций
3. COPY: копирует файлы или директории из локальной файловой системы в образ
4. RUN: выполняет команды во время сборки образа
5. CMD: указывает команду, которая будет выполнена при запуске контейнера

**Docker Compose**(`docker-compose.yml`) - это инструмент, который позволяет определять и запускать многоконтейнерные приложения с помощью простого YAML-файла.  <br>
Основные команды Dokcer-Compose
```docker-compose up``` - запуск приложения
```docker-compose down``` - удаление контейнеров
```docker-compose build``` - сборка образов
```docker-compose ps``` - просмотр состояния
```docker-compose logs``` - показывает логи контейнеров

## CI/CD
Continuous Integration/Continuous Delivery/Deployment - это методология, направленная н автоматизацию процессов разработки, тестирования и доставки ПО.
1. **Continuous Integration (CI)**
Непрерывная интеграция - практика частого слияния кода разработчиков в общий репозиторий. Каждое изменение автоматически проверяется на ошибки с помощью:
- Автоматических тестов (юнит-тесты, интеграционные тесты).
- Статического анализа кода (проверка стиля, уязвимостей).
- Сборки проекта (компиляция, создание артефактов).<br>
Цель: Ранее обнаружение конфликтов и ошибок.
2. **Continuous Delivery (CD)**
Непрерывная доставка - автоматизация подготовки кода к релизу. После CI код автоматически развертывается в тестовые среды (staging, QA), где проводится ручное или автоматическое тестирование.
Цель: Готовность кода к выпуску в любой момент.
3. **Continuous Deployment**
Расширение Continuous Delivery, где каждый успешно протестированный коммит автоматичеси попадает в продакшен-среду.
Цель:Минимизация времени между разработкой и выпуском.

### Принципы CI/CD
- Автоматизация всех этапов<br>
Ручные действия заменяются скриптами и пайплайнами (например, через Jenkins, GitLab CI/CD).
- Частые и мелкие коммиты<br>
Чем меньше изменений в одном коммите — тем проще найти и исправить ошибки.
- Изолированные среды<br>
Тестирование и развертывание выполняются в средах, идентичных продакшену (Docker, виртуализация).
- Мониторинг и обратная связь<br>
По
сле деплоя собираются метрики работы приложения (логи, производительность), чтобы быстро реагировать на проблемы.
- Идемпотентность<br>
Каждый запуск пайплайна дает одинаковый результат, независимо от окружения.
#### Основные этапы CI/CD pipeline:
- Сборка(Build): Компиляция кода, создание Docker-образов
- Тестирование(Test): Запуск юнит-тестов, проверка безопасности
- Деплой в тестовое окружение: Развертывание на staging-сервере
- Ручное тестирование(опционально): QA-инженеры проверяют функционал
- Деплой в прод: Автоматическое или ручное развертывание
## Jenkins
это open-source платформа для автоматизации CI/CD, позволяющая автоматизировать процессы
сборки, тестирования и развертывания приложений.
- Автоматизация процессов
- Поддержка плагинов
- Кроссплатформенность
Запуск ```sudo systemctl start jenkins```
```sudo systemctl enable jenkins```

## Kubernetes(K8s)
Это платформа для автоматизации развертывания, масштабирования и управления контейнеризированными приложениями. С помощью него можно управлять контейнерами в кластере, автоматичкски маштабировать приложения, обеспечивать отказоустойчивость и высокую досупность.
**Основные концепции**
-***Кластер (Cluster)*** Наборузлов (нод), на которых запускаются контейнеры.
-***Node (Узел)*** Физическая или виртуальная машина, на которой запускаются контейнеры.
-***Pod*** Минимальная единица развертывания в Kubernetes, которая может содержать один или несколько контейнеров
-***Deployment*** Описание желаемого состояния приложения, включая количество реплик и стратегию обновления
-***Service*** Абстракиця для доступа к приложению, работающая в кластере
-***Namespace*** Виртуальный кластер внутри физического кластера, используемый для изоляции ресурсов

**Minikube** — это инструмент для локального запуска Kubernetes-кластера на одной машине.
