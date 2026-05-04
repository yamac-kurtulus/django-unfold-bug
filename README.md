This is a demo project to showcase bug in [Unfold-admin:#2017](https://github.com/unfoldadmin/django-unfold/issues/2017)

django-unfold 0.87.0 bug: `RangeDateFilter` can fail on first use when the
same changelist also renders Django admin date widgets from `list_editable`.

Setup:

1. `cd demo`
2. `../.venv/bin/python manage.py migrate`
3. `../.venv/bin/python manage.py seed_bugdemo`
4. `../.venv/bin/python manage.py runserver`
5. Open `http://127.0.0.1:8000/admin/`
6. Login with `admin` / `admin`
7. Open `Reports`

How to reproduce:

1. In the right sidebar, open the `filter_date` range calendar.
2. On first load, click any date in the current month.
3. The popup closes, but the selected value is not written into the filter input.
4. Click next/previous month once, or choose `Yesterday`, `Today`, or `Tomorrow`.
5. After that, date selection starts working normally.

Notes:

- `editable_date` is in `list_editable`, so Django admin date widgets are
  rendered in the changelist table.
- Those `editable_date` inputs work normally. Only the Unfold range-date
  filter inputs are affected.
