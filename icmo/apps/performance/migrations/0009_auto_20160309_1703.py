# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0008_auto_20160114_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='apr_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='apr_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='apr_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='apr_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='apr_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='apr_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='apr_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='apr_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='apr_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='apr_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='aug_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='aug_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='aug_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='aug_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='aug_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='aug_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='aug_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='aug_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='aug_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='aug_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='dec_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='dec_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='dec_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='dec_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='dec_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='dec_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='dec_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='dec_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='dec_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='dec_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='feb_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='feb_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='feb_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='feb_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='feb_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='feb_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='feb_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='feb_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='feb_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='feb_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='fiscal_year_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='fiscal_year_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='fiscal_year_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='fiscal_year_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='fiscal_year_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='fiscal_year_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='fiscal_year_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='fiscal_year_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='fiscal_year_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jan_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jan_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jan_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jan_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jan_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jan_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jan_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jan_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jan_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jan_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jul_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jul_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jul_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jul_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jul_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jul_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jul_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jul_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jul_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jul_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jun_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jun_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jun_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jun_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jun_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jun_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jun_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jun_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jun_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='jun_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='mar_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='mar_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='mar_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='mar_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='mar_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='mar_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='mar_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='mar_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='mar_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='mar_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='may_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='may_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='may_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='may_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='may_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='may_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='may_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='may_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='may_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='may_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='nov_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='nov_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='nov_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='nov_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='nov_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='nov_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='nov_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='nov_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='nov_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='nov_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='oct_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='oct_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='oct_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='oct_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='oct_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='oct_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='oct_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='oct_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='oct_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='oct_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q1_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q1_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q1_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q1_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q1_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q1_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q1_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q1_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q1_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q1_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q2_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q2_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q2_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q2_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q2_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q2_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q2_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q2_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q2_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q2_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q3_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q3_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q3_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q3_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q3_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q3_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q3_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q3_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q3_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q3_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q4_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q4_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q4_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q4_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q4_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q4_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q4_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q4_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q4_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='q4_touches_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='sep_contacts',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='sep_contacts_to_mql_conversion',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='sep_cost',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='sep_cost_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='sep_cost_per_mql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='sep_cost_per_mql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='sep_cost_per_sql',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='sep_cost_per_sql_currency',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='sep_touches',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='sep_touches_to_mql_conversion',
        ),
        migrations.AddField(
            model_name='campaign',
            name='apr_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='aug_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='dec_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='feb_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='fiscal_year_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='jan_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='jul_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='jun_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='mar_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='may_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='nov_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='oct_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='q1_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='q2_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='q3_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='q4_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='sep_sql_to_sale_conversion',
            field=core.fields.PercentField(default=0, max_digits=4, decimal_places=1),
        ),
    ]