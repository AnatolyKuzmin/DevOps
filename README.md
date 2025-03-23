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
-***Pod*** Минимальная единица развертывания в Kubernetes, которая может содержать один или несколько контейнеров. ```kubectl get pods``` просмотр списка Pods, ```kubectl describe pod <pod_name>``` подробная информация о Pod, ```kubectl logs <pod_name>``` просмотр логов Pod, ```kubectl delete pod <pod_name>``` удаление Pod.  
-***Deployment*** Описание желаемого состояния приложения, включая количество реплик и стратегию обновления. ```kubectl get deployments``` просмотр списка Deployments, ```kubectl describe deployment <deployment_name>``` подробная информация о Deployment, ```kubectl delete deployment <deployment_name>``` удаление Deployment, ```kubectl scale deployment my-deployment --replicas=5``` Масштабируйте количество реплик до 5.  
-***Service*** Абстракиця для доступа к приложению, работающая в кластере  
-***Namespace*** Виртуальный кластер внутри физического кластера, используемый для изоляции ресурсов  

**Архитектура Kubernetes**  
Kubernetes работает по схеме "ведущий-ведомый". ***Мастер-нода (Control Plane)*** управляет кластером. В неё входит kube-apiserver которая принимает запросы и управляет кластером, kube-scheduler распределяет поды по нодам, kube-controller-manager отслеживает состояние кластера, etcd хранилище конфигураций и данных о состоянии кластера. ***Рабочие ноды (WorkerNodes)*** выполняют задачи. Включают kubelet агент управляющий подами на ноде, kube-proxy обеспечивает сетевую свзяность между подами

**Minikube** — это инструмент для локального запуска Kubernetes-кластера на одной машине.  
Установка ```curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube```  
Проверка ```minikube version```  
**kubectl** — командная строка для управления Kubernetes  
Установка ```curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl```  
Проверка ```kubectl version --client```  
Посмотреть узлы в кластере ```kubectl get nodes```  
Простеший pod.yaml  
```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
```  
```kubectl apply -f pod.yaml```  Применить конфигурацию, ```kubectl get pods```  Просмотреть список Pods, ```kubectl delete pod my-pod```  Удалить Pod  

Файл deployment.yaml  
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: ваш-username/my-python-app:v1.0
        ports:
        - containerPort: 5000
```  
Файл service.yaml  
```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: LoadBalancer
```   

**Пробный запус**: 1. `minikube start [--driver=docker]/[--driver=virtualbox]` Запустите Minikube, 2. `minikube status` Проверьте статус кластера, 3. `kubectl apply -f deployment.yaml` Примените конфигурацию, 3.1. `kubectl get deployments` Просмотреть список Deployments  , 4. `kubectl apply -f service.yaml` Примените конфигурацию, 4.1. `kubectl get services` Просмотреть список Services, 4.2. `minikube service my-service` Открыть приложение в браузере ,  5. `minikube ip` Получите IP кластера, 5. `kubectl get svc my-service -o jsonpath='{.spec.ports[0].nodePort}'` Получите порт сервиса 6. `kubectl scale deployment my-deployment --replicas=5` Масштабируйте развертывание, 7. `kubectl get pods` Проверьте количество подов, 8. `minikube dashboard` Открыть дашборд Kubernetes, 9. `minikube stop` Остановите кластер, 10. `minikube delete` Удалите кластер

Сервис (Service) в Kubernetes - это абстракция, котоаря определяет набор Pods и политику доступа к ним. Сервисы обеспечивают стабильный IP-адрес и DNS-имя для набора Pods. Распределяют нагрузку между Pods. Обеспечивают доступ к приложениям внутри и вне кластера.  
Типы сервисов: **ClusterIP** (по умолчанию) сервис доступен только внутри кластера; **NodePort** сервис доступен через статичный порт на каждом узле кластера; **LoadBalancer** сервис доступен через внешний балансировщик нагрузки; **ExternalName** сервис предоставляет DNS-имя для внешнего ресурса.

***Ingress*** - это объект Kubernetes, который управляет внешним доступом к сервисам в кластере.  
Ingress позволяет:  
- Настраивать маршрутизацию HTTP/HTTPS трафика.  
- Управлять доменными именами и SSL/TLS сертификатами.
- Обеспечивать доступ к нескольким сервисам через один IP-адрес.

Основные команды для работы с сервисами Ingress  
`kubectl get services` просмотр списка сервисов. `kubectl describe service <service_name>` подробная информация о сервисе. `kubectl get ingress` просмотр списка Ingress. `kubectl describe ingress <ingress_name>` подробная информация о Ingress. `kubectl apply -f <file.yaml>` применение конфигурации из файла. `kubectl delete service <service_name>` удаление сервиса. `kubectl delete ingress <ingress_name>` удаление Ingress.

Файл ingress.yaml  
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: my-app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-service
            port:
              number: 80
```   

Установить Ingress-контроллер (например, Nginx Ingress Controller)  
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.0.0/deploy/static/provider/cloud/deploy.yaml
```

**Пробный запус**: 1. `minikube start [--driver=docker]/[--driver=virtualbox]` Запустите Minikube, 2. `kubectl apply -f service.yaml` Примените конфигурацию, 3. `kubectl apply -f ingress.yaml` Примените конфигурацию, 4. `kubectl get services` Просмотреть список Ingress,  5. `kubectl describe ingress my-ingress` Просмотритm подробную информацию о Ingress, 6. `echo "$(minikube ip) my-app.example.com" | sudo tee -a /etc/hosts` запись в файл /etc/hosts для тестирования, 7. `http://my-app.example.com` Откройтm приложение в браузере, 8. `kubectl delete service my-service` Удалить сервис, 9. ` kubectl delete ingress my-ingress` Удалить Ingress, 10. `minikube stop` Остановите кластер, 11. `minikube delete` Удалите кластер

**Volumes** - это механизм для хранения данных в Kubernetes. Volumes позволяют: Сохранять данные между запусками Pods; Обмениваться данными между контейнерами внутри Pods; Подключать внешние хранилища данных.  
Типы Volumes:  
- emptyDir: временное хранилище, которое существует только пока Pod запущен.  
- hostPath: монтирует файловую систему узла (ноды) в Pod.  
- Persistent Volume (PV): постоянное хранилище, которое существует независимо от Pods.  
- Persistent Volume Claim (PVC): запрос на выделение Persistent Volume.

***Persistent Volume (PV)*** — это ресурс в кластере, представляющий собой физическое хранилище данных. PV может быть:  
- Статическим: создается администратором кластера.  
- Динамическим: создается автоматически при запросе PVC.  

Основные команды для работы с Volumes и PVC  
`kubectl get pv` просмотр списка Persistent Volumes. `kubectl get pvc` просмотр списка Persistent Volume Claims. `kubectl describe pv <pv_name>` подробная информация о Persistent Volume. `kubectl describe pvc <pvc_name>` подробная информация о Persistent Volume Claim.. `kubectl apply -f <file.yaml>` применение конфигурации из файла. `kubectl delete pv <pv_name>` удаление Persistent Volume. `kubectl delete pvc <pvc_name>` удаление Persistent Volume Claim.

Файл pv.yaml  
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /mnt/data
```
Файл pvc.yaml  
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Файл pod.yaml(PVC в Pod)  
```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    volumeMounts:
    - mountPath: "/usr/share/nginx/html"
      name: my-storage
  volumes:
  - name: my-storage
    persistentVolumeClaim:
      claimName: my-pvc
```

**Пробный запус**: 1. `minikube start [--driver=docker]/[--driver=virtualbox]` Запустите Minikube, 2. `kubectl apply -f pv.yaml` Примените конфигурацию, 2.1. `kubectl get pv` Просмотрите список Persistent Volumes, 3. `kubectl apply -f pvc.yaml` Примените конфигурацию, 3.1. `kubectl get pvc` Просмотрите список Persistent Volume Claims, 4. `kubectl apply -f pod.yaml` Примените конфигурацию, 4.1. `kubectl get pods` Просмотрите список Pods, 5. `kubectl exec -it my-pod -- /bin/sh` Подключитесь к Pod, 6. `ls /usr/share/nginx/html` Проверьте, что том смонтирован, 7. `echo "Hello, Kubernetes!" > /usr/share/nginx/html/index.html` Создайте файл в томе, 8. `cat /usr/share/nginx/html/index.html` Проверьте содержимое файла, 9. `kubectl delete pod my-pod` Удалите Pod, 9.1. `kubectl delete pvc my-pvc` Удалите PVC, 9.2. `kubectl delete pvc my-pvc` Удалите PV, 10. `minikube stop` Остановите кластер, 11. `minikube delete` Удалите кластер

**Helm** — это менеджер пакетов для Kubernetes, который позволяет: Упрощать установку и управление приложениями; Использовать шаблоны для настройки ресурсов Kubernetes; Управлять версиями приложений с помощью чартов. ***Чарт (Chart)*** пакет, содержащий описание ресурсов Kubernetes и шаблоны для их настройки. ***Релиз (Release)*** экземпляр чарта, развернутый в кластере Kubernetes. ***Репозиторий (Repository)*** хранилище чартов, доступное для установки.  
Основные команды Helm  
`helm install` установка чарта в кластер. `helm upgrade` обновление релиза. `helm uninstall` удаление релиза. `helm list` подробная информация о Persistent Volume Claim. `helm repo add` добавление репозитория чартов. `helm search` поиск чартов в репозиториях.
