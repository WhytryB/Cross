from django.contrib import admin
from aqsa_apps.wallet_tag_etc.models import Wallet,Category,Tag,Contact,Goal
from aqsa_apps.transaction.models import Transaction


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'currency')
    list_filter = ('owner', 'currency')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    list_filter = ('owner', 'name')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',)
    list_filter = ('owner', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    list_filter = ('owner', 'name')


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner','goal_total','wallet12')
    list_filter = ('owner', 'goal_total')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'transfer', 'date', 'value', 'wallet', 'bank_date')
    list_filter = ('owner', 'transfer', 'date', 'value', 'wallet', 'bank_date')
    date_hierarchy = 'bank_date'