# Agent Skills & Task Instructions

Ниже описаны типовые задачи (навыки), которые Codex должен уметь выполнять по запросу пользователя.

---

## Skill 1: Generate Test Cases (`/test-cases`)
**Trigger:** Пользователь просит написать тест-кейсы на фичу, ручку API или UI-экран.

**Instructions:**
1. Проанализируй входящие требования или структуру API/UI.
2. Раздели кейсы на 3 категории:
   - **Smoke / Positive Path** (основной зеленый сценарий)
   - **Negative / Validation** (ошибки ввода, 4xx/5xx ответы, неверные права)
   - **Edge Cases & Security** (граничные значения, спецсимволы, XSS/SQLi на базовом уровне)
3. Форматируй в Markdown-таблицу или списки с полями: ID, Title, Priority, Steps, Expected Result.

---

## Skill 2: Write API Tests (`/api-test`)
**Trigger:** Пользователь просит покрыть API-эндпоинт автотестами.

**Instructions:**
1. Создай или обнови Pydantic-модель ответа в `models/`.
2. Напиши кастомный API-клиент или используй `requests.Session`.
3. Напиши Pytest-функцию:
   - Добавь `@allure.title` и `@allure.feature`.
   - Оберни HTTP-вызов и валидацию статуса в `with allure.step(...)`.
   - Выполни проверку статус-кода и валидацию Pydantic-схемы.

---

## Skill 3: Write Web/Mobile UI Test (`/ui-test`)
**Trigger:** Пользователь просит написать Web (Selenium) или Mobile (Appium) автотест.

**Instructions:**
1. Вынеси элементы и действия в класс страницы/экрана (`Page Object`).
2. Используй только надежные локаторы: `By.ACCESSIBILITY_ID` / `By.ID` в приоритете, затем `By.XPATH` (избегать длинных абсолютных путей).
3. Используй `WebDriverWait` и `expected_conditions` для поиска элементов.
4. В самом тесте оставь только высокоуровневые шаги без прямого обращения к драйверу.

---

## Skill 4: Refactor Flaky / Bad Test (`/refactor-test`)
**Trigger:** Пользователь показывает упавший или "плавающий" тест.

**Instructions:**
1. Найди антипаттерны (`time.sleep`, незакрытые сессии, зависимость от порядка выполнения, завязка на динамические ID).
2. Замени `time.sleep()` на явные ожидания или polling.
3. Вынеси повторяющийся код в Pytest-фикстуры.
4. Объясни кратко, в чем была проблема и как рефакторинг её устранил.