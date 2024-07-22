from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from store.models import Item, Category
from management.forms import ItemForm, CategoryForm, UserCreationFormWithPassword, UserUpdateForm
from django.contrib import messages
from .mixins import AdminRequiredMixin
from django.contrib.auth.models import User



# Item Views
class ItemListView(AdminRequiredMixin, View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, 'management/item_list.html', {'items': items})

class ItemCreateView(AdminRequiredMixin, View):
    def get(self, request):
        form = ItemForm()
        return render(request, 'management/item_form.html', {'form': form})

    def post(self, request):
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item was successfully created.')
            return redirect('management:item_list')
        for error in form.errors.values():
            messages.error(request, error)
        return render(request, 'management/item_form.html', {'form': form})

class ItemUpdateView(AdminRequiredMixin, View):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        form = ItemForm(instance=item)
        return render(request, 'management/item_form.html', {'form': form})

    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item was successfully updated.')
            return redirect('management:item_list')
        for error in form.errors.values():
            messages.error(request, error)
        return render(request, 'management/item_form.html', {'form': form})


class ItemDeleteView(AdminRequiredMixin, View):
    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item_name = item.name
        item.delete()
        messages.success(request, f'Item "{item_name}" was successfully deleted.')
        return redirect('management:item_list')

# Category Views
class CategoryListView(AdminRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'management/category_list.html', {'categories': categories})

class CategoryCreateView(AdminRequiredMixin, View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'management/category_form.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category was successfully created.')
            return redirect('management:category_list')
        for error in form.errors.values():
            messages.error(request, error)
        return render(request, 'management/category_form.html', {'form': form})

class CategoryUpdateView(AdminRequiredMixin, View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(instance=category)
        return render(request, 'management/category_form.html', {'form': form})

    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category was successfully updated.')
            return redirect('management:category_list')
        for error in form.errors.values():
            messages.error(request, error)
        return render(request, 'management/category_form.html', {'form': form})

class CategoryDeleteView(AdminRequiredMixin, View):
    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category_name = category.name
        category.delete()
        messages.success(request, f'Category "{category_name}" was successfully deleted.')
        return redirect('management:category_list')

# User Views
class UserListView(AdminRequiredMixin, View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'management/user_list.html', {'users': users})

class UserCreateView(AdminRequiredMixin, View):
    def get(self, request):
        form = UserCreationFormWithPassword()
        return render(request, 'management/user_form.html', {'form': form, 'title': 'Create User'})

    def post(self, request):
        form = UserCreationFormWithPassword(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User was successfully created.')
            return redirect('management:user_list')
        for error in form.errors.values():
            messages.error(request, error)
        return render(request, 'management/user_form.html', {'form': form, 'title': 'Create User'})

class UserUpdateView(AdminRequiredMixin, View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserUpdateForm(instance=user)
        return render(request, 'management/user_form.html', {'form': form, 'title': 'Update User'})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User was successfully updated.')
            return redirect('management:user_list')
        for error in form.errors.values():
            messages.error(request, error)
        return render(request, 'management/user_form.html', {'form': form, 'title': 'Update User'})

class UserDeleteView(AdminRequiredMixin, View):
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user_name = user.username
        user.delete()
        messages.success(request, f'User "{user_name}" was successfully deleted.')
        return redirect('management:user_list')
