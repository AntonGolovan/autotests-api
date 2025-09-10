# Autotests API

Проект автоматизированного тестирования API для системы управления кампаниями и креативами. Проект построен на основе современного стека технологий Python с использованием pytest, httpx, Pydantic и других инструментов.

## 📋 Содержание

- [Описание проекта](#описание-проекта)
- [Архитектура](#архитектура)
- [Структура проекта](#структура-проекта)
- [Технологический стек](#технологический-стек)
- [Установка и настройка](#установка-и-настройка)
- [Запуск тестов](#запуск-тестов)
- [Компоненты системы](#компоненты-системы)
- [Примеры использования](#примеры-использования)

## 🎯 Описание проекта

Данный проект представляет собой комплексную систему автоматизированного тестирования API для CRM-системы управления маркетинговыми кампаниями. Система позволяет:

- **Создавать и управлять кампаниями** - тестирование полного жизненного цикла кампаний от создания до завершения
- **Работать с креативами** - создание и управление креативными материалами для кампаний
- **Валидировать API** - проверка корректности ответов сервера и соответствия схеме данных
- **Генерировать тестовые данные** - автоматическое создание реалистичных тестовых данных

## 🏗️ Архитектура

Проект построен по принципу **Page Object Model** (POM), адаптированному для API-тестирования:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Test Layer    │    │  Client Layer   │    │  Schema Layer   │
│                 │    │                 │    │                 │
│ • test_*.py     │───▶│ • *_client.py   │───▶│ • *_schema.py   │
│ • Fixtures      │    │ • API calls     │    │ • Data models   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Assertion Layer │    │   HTTP Layer    │    │  Utility Layer  │
│                 │    │                 │    │                 │
│ • assertions/   │    │ • httpx         │    │ • fakers.py     │
│ • validations   │    │ • APIClient     │    │ • helpers       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📁 Структура проекта

```
autotests-api/
├── clients/                    # API клиенты
│   ├── api_client.py          # Базовый HTTP клиент
│   ├── client_builder.py      # Фабрика клиентов
│   ├── campaign/              # Клиент для работы с кампаниями
│   │   ├── campaign_client.py
│   │   └── models/
│   │       └── campaign_schema.py
│   └── creative/              # Клиент для работы с креативами
│       ├── creative_client.py
│       └── models/
│           └── creative_schema.py
├── fixtures/                  # Pytest фикстуры
│   ├── campaign_fixture.py
│   └── creative_fixture.py
├── tests/                     # Тестовые сценарии
│   ├── campaign/
│   │   └── test_campaign.py
│   └── creative/
│       └── test_creative.py
├── tools/                     # Вспомогательные инструменты
│   ├── assertions/           # Кастомные проверки
│   │   ├── base.py
│   │   ├── campaign.py
│   │   ├── creative.py
│   │   └── schema.py
│   └── fakers.py            # Генератор тестовых данных
├── testdata/                 # Тестовые данные
│   └── files/
│       └── image.png
├── conftest.py              # Конфигурация pytest
├── pytest.ini              # Настройки pytest
├── requirements.txt         # Зависимости проекта
└── README.md               # Документация
```

## 🛠️ Технологический стек

### Основные библиотеки

- **pytest** (7.4.0) - фреймворк для тестирования
- **httpx** (0.28.1) - современный HTTP клиент для асинхронных и синхронных запросов
- **Pydantic** (2.11.7) - валидация данных и сериализация/десериализация
- **Faker** (37.6.0) - генерация реалистичных тестовых данных
- **jsonschema** (4.25.1) - валидация JSON схем

### Дополнительные инструменты

- **python-dateutil** - работа с датами и временем
- **typing-extensions** - расширенные типы для Python
- **certifi** - SSL сертификаты для HTTPS запросов

## ⚙️ Установка и настройка

### Предварительные требования

- Python 3.8+
- pip (менеджер пакетов Python)

### Установка зависимостей

```bash
# Клонирование репозитория
git clone <repository-url>
cd autotests-api

# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
```

### Настройка окружения

Проект настроен для работы с тестовым окружением:
- **Base URL**: `https://qq.taxi.tst.yandex-team.ru/api-t/admin/crm_admin`
- **Timeout**: 5 секунд

## 🚀 Запуск тестов

### Основные команды

```bash
# Запуск всех тестов
pytest

# Запуск с подробным выводом
pytest -v -s

# Запуск тестов кампаний
pytest tests/campaign/

# Запуск тестов креативов
pytest tests/creative/

# Запуск тестов по маркерам
pytest -m smoke          # Дымовые тесты
pytest -m regression     # Регрессионные тесты
pytest -m test_creative  # Тесты креативов
```

### Параметры pytest

Настройки в `pytest.ini`:
- `-s` - отключение захвата вывода
- `-v` - подробный режим
- Автоматическое обнаружение тестов по паттернам `test_*.py` и `*_tests.py`

## 🔧 Компоненты системы

### 1. API Клиенты

#### APIClient (Базовый клиент)
```python
class APIClient:
    """Базовый HTTP клиент с методами для всех типов запросов"""
    
    def get(url, params=None)     # GET запросы
    def post(url, json=None)      # POST запросы  
    def patch(url, json=None)     # PATCH запросы
    def delete(url)               # DELETE запросы
```

**Зачем нужен**: Предоставляет единообразный интерфейс для всех HTTP операций, инкапсулирует работу с httpx, добавляет общую функциональность (логирование, обработка ошибок).

#### CampaignClient
```python
class CampaignClient(APIClient):
    """Специализированный клиент для работы с кампаниями"""
    
    def get_campaign_api(campaign_id)           # Получение кампании
    def create_campaign_api(request)            # Создание кампании
    def update_campaign_api(campaign_id, request) # Обновление кампании
    def create_campaign(request)                # Создание с валидацией
```

**Зачем нужен**: Инкапсулирует всю логику работы с API кампаний, предоставляет типизированные методы, автоматически обрабатывает сериализацию/десериализацию данных.

#### CreativeClient
```python
class CreativeClient(APIClient):
    """Специализированный клиент для работы с креативами"""
    
    def create_creative_map_api(campaign_id, request)  # Создание карты креативов
    def get_creative_maps_api(campaign_id)             # Получение карт креативов
    def create_creative_cms_api(request)               # Создание креатива в CMS
```

**Зачем нужен**: Управляет сложной логикой работы с креативами, включая создание карт креативов и связывание их с кампаниями.

### 2. Модели данных (Pydantic схемы)

#### Campaign Schema
- **CreateCampaignRequestSchema** - данные для создания кампании
- **CreateCampaignResponseSchema** - ответ сервера при создании
- **UpdateCampaignRequestSchema** - данные для обновления
- **CampaignStateSchema** - состояния кампании (NEW, READY, COMPLETED, etc.)

#### Creative Schema  
- **CreateCreativeMapRequestSchema** - создание карты креативов
- **CreateCreativeCmsRequestSchema** - создание креатива в CMS
- **LocaleWithContentSchema** - локализованный контент
- **MediaSchema** - медиа материалы

**Зачем нужны**: Обеспечивают типизацию данных, автоматическую валидацию, сериализацию/десериализацию JSON, автодополнение в IDE.

### 3. Фикстуры (Fixtures)

#### CampaignFixture
```python
class CampaignFixture(BaseModel):
    request: CreateCampaignRequestSchema
    response: CreateCampaignResponseSchema
    
    @property
    def campaign_id(self) -> int
    @property  
    def planned_channel(self) -> list[str]
```

#### CreativeMapFixture
```python
class CreativeMapFixture(BaseModel):
    request: CreateCreativeMapRequestSchema
    response: CreateCreativeMapResponseSchema
```

**Зачем нужны**: Упрощают создание тестовых данных, обеспечивают переиспользование объектов между тестами, автоматически управляют жизненным циклом тестовых сущностей.

### 4. Система проверок (Assertions)

#### Базовые проверки
```python
def assert_status_code(actual, expected)    # Проверка HTTP статуса
def assert_equal(actual, expected, name)    # Проверка равенства значений
def assert_is_true(actual, name)            # Проверка истинности
```

#### Специализированные проверки
```python
def assert_create_campaign(request, response)           # Проверка создания кампании
def assert_creative_map(request, response)              # Проверка карты креативов
def validate_json_schema(instance, schema)              # Валидация JSON схемы
```

**Зачем нужны**: Обеспечивают единообразные и информативные сообщения об ошибках, инкапсулируют сложную логику проверок, упрощают написание тестов.

### 5. Генератор тестовых данных (Fakers)

```python
class Fake:
    def text() -> str                    # Случайный текст
    def email(domain=None) -> str        # Email адрес
    def uuid4() -> str                   # UUID
    def integer(start=1, end=100) -> int # Случайное число
    def sentence() -> str                # Предложение
```

**Зачем нужен**: Генерирует реалистичные тестовые данные, обеспечивает уникальность данных в тестах, упрощает создание тестовых сценариев.

## 📝 Примеры использования

### Создание кампании

```python
def test_create_campaign(campaign_client: CampaignClient):
    # Создание запроса с тестовыми данными
    request = CreateCampaignRequestSchema(
        name="Тестовая кампания",
        specification="Описание кампании",
        planned_channels=["user_push"]
    )
    
    # Отправка запроса
    response = campaign_client.create_campaign_api(request)
    
    # Проверки
    assert_status_code(response.status_code, HTTPStatus.OK)
    response_data = CreateCampaignResponseSchema.model_validate_json(response.text)
    assert_create_campaign(request, response_data)
```

### Работа с креативами

```python
def test_creative_workflow(campaign: CampaignFixture, creative_client: CreativeClient):
    # Создание карты креативов
    map_request = CreateCreativeMapRequestSchema(
        creative_map_name="Тестовая карта",
        communication_channel=campaign.planned_channel
    )
    
    map_response = creative_client.create_creative_map(
        campaign_id=campaign.campaign_id, 
        request=map_request
    )
    
    # Создание креатива в CMS
    cms_request = CreateCreativeCmsRequestSchema(
        communication_channel="object_over_map",
        creative_map_id_with_version=CreativeMapIdWithVersionSchema(
            id=map_response.creative_map_id,
            version=1
        )
    )
    
    cms_response = creative_client.create_creative_cms(cms_request)
    
    # Проверка связи между картой и креативом
    assert_relation_creative_map_with_creative_cms(cms_response, map_response)
```

### Использование фикстур

```python
def test_campaign_lifecycle(campaign: CampaignFixture, campaign_client: CampaignClient):
    # Фикстура автоматически создает кампанию
    assert campaign.campaign_id > 0
    assert len(campaign.planned_channel) > 0
    
    # Получение созданной кампании
    response = campaign_client.get_campaign_api(str(campaign.campaign_id))
    assert_status_code(response.status_code, HTTPStatus.OK)
```

## 🏷️ Маркеры тестов

Проект использует pytest маркеры для категоризации тестов:

- `@pytest.mark.smoke` - дымовые тесты (быстрые, критичные)
- `@pytest.mark.regression` - регрессионные тесты (полное покрытие)
- `@pytest.mark.test_creative` - тесты креативов
- `@pytest.mark.users` - тесты пользователей
- `@pytest.mark.authentication` - тесты аутентификации

## 🔍 Мониторинг и отладка

### Логирование
Все HTTP запросы логируются автоматически через httpx. Для включения подробного логирования:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Отладка тестов
```bash
# Запуск с отладочной информацией
pytest -v -s --tb=long

# Запуск конкретного теста
pytest tests/campaign/test_campaign.py::TestCampaign::test_create_campaign -v -s
```

## 📊 Покрытие тестами

Проект обеспечивает комплексное тестирование:

- ✅ **Функциональное тестирование** - проверка корректности API
- ✅ **Валидация данных** - проверка схем и типов данных  
- ✅ **Интеграционное тестирование** - тестирование взаимодействия компонентов
- ✅ **Регрессионное тестирование** - проверка стабильности после изменений

## 🤝 Вклад в проект

1. Создайте feature ветку
2. Добавьте тесты для новой функциональности
3. Убедитесь, что все тесты проходят
4. Создайте Pull Request

## 📞 Поддержка

При возникновении вопросов или проблем:
1. Проверьте документацию
2. Изучите примеры в папке `tests/`
3. Обратитесь к команде разработки

---

**Версия проекта**: 1.0.0  
**Последнее обновление**: 2025  
**Автор**: Команда разработки автотестов
