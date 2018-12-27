# Author of Aqsa: Yulay Musin
# from django.contrib.auth.decorators import login_required
# from aqsa_apps.wallet_tag_etc import models as wte_m
# from aqsa_apps import sql_custom as sql
# from aqsa_apps.transaction import models as ta_m
# from aqsa_apps.wallet_tag_etc import currencies
# from django.shortcuts import render
# from django.utils.translation import ugettext as _
# from django.shortcuts import render_to_response
# from django.shortcuts import render_to_response
# from django.template.context import RequestContext

from aqsa_apps.wallet_tag_etc import viewxins_mixins as vxmx
from aqsa_apps.wallet_tag_etc import models as m
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from aqsa_apps.transaction import models as ns


class List(vxmx.List):
    model = m.Goal
    model_labels_and_fields = ('name','goal_total')
    context = {
        'title': _('GOal'),
        'msg_empty_object_list': _('You do not have any goal. Click to "New Goal" button for create it!'),
    }


class Create(vxmx.Create):
    template_name = 'common/form_goal.html'
    model = m.Goal
    fields = ['name','goal_total','wallet12']
    success_url = reverse_lazy('wallet_tag_etc:goal_list')
    success_url2 = reverse_lazy('wallet_tag_etc:goal_new')

    success_message = _('Goal have been created.')
    same_name_error_msg = _('You already have a goal with the same name. '
                            'Do not get confused in the future, type another name')




class Update(vxmx.Update):
    model = m.Goal
    fields = ['name','goal_total','wallet1_id']
    success_message = _('The goal was updated.')
    context = {
        'title': _('Edit Goal'),
    }


class Delete(vxmx.Delete):
    model = m.Goal
    success_message = _('The goal was deleted.')
    protected_error_msg = _('Could not delete this goal because one or more of your transactions linked to this '
                            'goal. Use filter in the list of transactions for find it!')
    context = {
        'title': _('Delete GOal'),
        'description': _('Are you sure you want to delete the goal shown below?'),
        'labels': [m.Goal._meta.get_field(label).verbose_name for label in List.model_labels_and_fields],
        'fields': List.model_labels_and_fields,
    }
