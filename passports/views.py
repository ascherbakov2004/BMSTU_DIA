from django.shortcuts import render, redirect, get_object_or_404
from .forms import BorderCrossingForm
from .models import BorderCrossingApplication, Passport, News
from django.contrib import messages

def passport_list(request):
    passports = Passport.objects.all()
    query = request.GET.get('query')
    if query:
        passports = passports.filter(full_name__icontains=query)
    for passport in passports:
        print(f"Passport: {passport.full_name}, Photo: {passport.photo.url}")
    return render(request, 'passport_list.html', {'passports': passports})


def passport_detail(request, pk):
    passport = get_object_or_404(Passport, pk=pk)
    return render(request, 'passport_detail.html', {'passport': passport})

def add_to_cart(request, passport_id):
    """Добавляет паспорт в корзину (сессию)"""
    passport = get_object_or_404(Passport, id=passport_id)
    cart = request.session.get('cart', [])

    if passport_id not in cart:
        cart.append(passport_id)
        request.session['cart'] = cart
        request.session.modified = True  # Фиксируем изменения в сессии

    cart = request.session.get('cart', [])  # Получаем корзину
    if passport_id not in cart:
        cart.append(passport_id)  # Добавляем паспорт, если его нет в корзине
    request.session['cart'] = cart  # Обновляем сессию
    request.session.modified = True  # Помечаем сессию как измененную
    return redirect('passport_list')


def cart_view(request):
    """Отображает список выбранных паспортов"""
    cart = request.session.get('cart', [])
    passports = Passport.objects.filter(id__in=cart)

    return render(request, 'cart.html', {'passports': passports})

def remove_from_cart(request, passport_id):
    """Удаляет паспорт из корзины (сессии)"""
    cart = request.session.get('cart', [])

    if passport_id in cart:
        cart.remove(passport_id)
        request.session['cart'] = cart
        request.session.modified = True  # Фиксируем изменения в сессии

    return redirect('cart_view')

def create_application(request):
    cart = request.session.get('cart', [])
    passports = Passport.objects.filter(id__in=cart)

    if request.method == "POST":
        print("Форма отправлена!")  # Отладка
        form = BorderCrossingForm(request.POST)
        if form.is_valid():
            print("Форма валидна!")  # Отладка
            application = form.save(commit=False)
            application.save()
            application.passports.set(passports)  # Привязываем паспорта к заявке
            request.session['cart'] = []  # Очищаем корзину
            return redirect('applications_list')  # Перенаправляем в список заявок
        else:
            print("Форма не валидна!")  # Отладка
            print(form.errors)  # Показываем ошибки формы
    else:
        form = BorderCrossingForm()

    return render(request, "application_form.html", {"form": form, "passports": passports})


def applications_list(request):
    applications = BorderCrossingApplication.objects.all()
    return render(request, "applications_list.html", {"applications": applications})

def confirm_crossing(request, application_id):
    application = get_object_or_404(BorderCrossingApplication, id=application_id)
    messages.success(request, f"Пересечение границы подтверждено для заявки {application.id}.")
    return redirect('applications_list')

def cancel_application(request, application_id):
    application = get_object_or_404(BorderCrossingApplication, id=application_id)
    application.delete()
    messages.success(request, f"Заявка {application.id} успешно отменена.")
    return redirect('applications_list')

def home(request):
    news_list = News.objects.all().order_by('-id')  # Последние новости сверху
    print(news_list)  # Выведет список новостей в консоли
    return render(request, "base.html", {"news_list": news_list})