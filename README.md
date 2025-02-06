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

## CI/CD
Continuous Integration/Continuous Delivery/Deployment - это методология, направленная н автоматизацию процессов разработки, тестирования и доставки ПО.
**Continuous Integration (CI)**
Непрерывная доставка - практика частого слияния кода разработчиков в общий репозиторий. Каждое изменение автоматически проверяется на ошибки с помощью:
- Автоматических тестов (юнит-тесты, интеграционные тесты).
- Статического анализа кода (проверка стиля, уязвимостей).
- Сборки проекта (компиляция, создание артефактов).
Цель: Ранее обнаружение конфликтов и ошибок.
