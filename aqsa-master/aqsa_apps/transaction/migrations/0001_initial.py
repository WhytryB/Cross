# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-18 11:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wallet_tag_etc', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer', models.BooleanField(db_index=True, default=False, verbose_name='Transfer or Income or Expense')),
                ('date', models.DateField(db_index=True, default=django.utils.timezone.now, verbose_name='Date')),
                ('value', models.DecimalField(db_index=True, decimal_places=2, max_digits=14, verbose_name='Value')),
                ('description', models.CharField(blank=True, default='', max_length=200, verbose_name='Description')),
                ('currency', models.PositiveSmallIntegerField(blank=True, choices=[(784, 'AED United Arab Emirates dirham'), (971, 'AFN Afghan afghani'), (8, 'ALL Albanian lek'), (51, 'AMD Armenian dram'), (532, 'ANG Netherlands Antillean guilder'), (973, 'AOA Angolan kwanza'), (32, 'ARS Argentine peso'), (36, 'AUD Australian dollar'), (533, 'AWG Aruban florin'), (944, 'AZN Azerbaijani manat'), (977, 'BAM Bosnia and Herzegovina convertible mark'), (52, 'BBD Barbados dollar'), (50, 'BDT Bangladeshi taka'), (975, 'BGN Bulgarian lev'), (48, 'BHD Bahraini dinar'), (108, 'BIF Burundian franc'), (60, 'BMD Bermudian dollar'), (96, 'BND Brunei dollar'), (68, 'BOB Boliviano'), (984, 'BOV Bolivian Mvdol (funds code)'), (986, 'BRL Brazilian real'), (44, 'BSD Bahamian dollar'), (64, 'BTN Bhutanese ngultrum'), (72, 'BWP Botswana pula'), (933, 'BYN Belarusian ruble'), (84, 'BZD Belize dollar'), (124, 'CAD Canadian dollar'), (976, 'CDF Congolese franc'), (947, 'CHE WIR Euro (complementary currency)'), (756, 'CHF Swiss franc'), (948, 'CHW WIR Franc (complementary currency)'), (990, 'CLF Unidad de Fomento (funds code)'), (152, 'CLP Chilean peso'), (156, 'CNY Renminbi (Chinese) yuan[8]'), (170, 'COP Colombian peso'), (970, 'COU Unidad de Valor Real (UVR) (funds code)[9]'), (188, 'CRC Costa Rican colon'), (931, 'CUC Cuban convertible peso'), (192, 'CUP Cuban peso'), (132, 'CVE Cape Verde escudo'), (203, 'CZK Czech koruna'), (262, 'DJF Djiboutian franc'), (208, 'DKK Danish krone'), (214, 'DOP Dominican peso'), (12, 'DZD Algerian dinar'), (818, 'EGP Egyptian pound'), (232, 'ERN Eritrean nakfa'), (230, 'ETB Ethiopian birr'), (978, 'EUR Euro'), (242, 'FJD Fiji dollar'), (238, 'FKP Falkland Islands pound'), (826, 'GBP Pound sterling'), (981, 'GEL Georgian lari'), (936, 'GHS Ghanaian cedi'), (292, 'GIP Gibraltar pound'), (270, 'GMD Gambian dalasi'), (324, 'GNF Guinean franc'), (320, 'GTQ Guatemalan quetzal'), (328, 'GYD Guyanese dollar'), (344, 'HKD Hong Kong dollar'), (340, 'HNL Honduran lempira'), (191, 'HRK Croatian kuna'), (332, 'HTG Haitian gourde'), (348, 'HUF Hungarian forint'), (360, 'IDR Indonesian rupiah'), (376, 'ILS Israeli new shekel'), (356, 'INR Indian rupee'), (368, 'IQD Iraqi dinar'), (364, 'IRR Iranian rial'), (352, 'ISK Icelandic króna'), (388, 'JMD Jamaican dollar'), (400, 'JOD Jordanian dinar'), (392, 'JPY Japanese yen'), (404, 'KES Kenyan shilling'), (417, 'KGS Kyrgyzstani som'), (116, 'KHR Cambodian riel'), (174, 'KMF Comoro franc'), (408, 'KPW North Korean won'), (410, 'KRW South Korean won'), (414, 'KWD Kuwaiti dinar'), (136, 'KYD Cayman Islands dollar'), (398, 'KZT Kazakhstani tenge'), (418, 'LAK Lao kip'), (422, 'LBP Lebanese pound'), (144, 'LKR Sri Lankan rupee'), (430, 'LRD Liberian dollar'), (426, 'LSL Lesotho loti'), (434, 'LYD Libyan dinar'), (504, 'MAD Moroccan dirham'), (498, 'MDL Moldovan leu'), (969, 'MGA Malagasy ariary'), (807, 'MKD Macedonian denar'), (104, 'MMK Myanmar kyat'), (496, 'MNT Mongolian tögrög'), (446, 'MOP Macanese pataca'), (929, 'MRU Mauritanian ouguiya'), (480, 'MUR Mauritian rupee'), (462, 'MVR Maldivian rufiyaa'), (454, 'MWK Malawian kwacha'), (484, 'MXN Mexican peso'), (979, 'MXV Mexican Unidad de Inversion (UDI) (funds code)'), (458, 'MYR Malaysian ringgit'), (943, 'MZN Mozambican metical'), (516, 'NAD Namibian dollar'), (566, 'NGN Nigerian naira'), (558, 'NIO Nicaraguan córdoba'), (578, 'NOK Norwegian krone'), (524, 'NPR Nepalese rupee'), (554, 'NZD New Zealand dollar'), (512, 'OMR Omani rial'), (590, 'PAB Panamanian balboa'), (604, 'PEN Peruvian Sol'), (598, 'PGK Papua New Guinean kina'), (608, 'PHP Philippine piso[13]'), (586, 'PKR Pakistani rupee'), (985, 'PLN Polish złoty'), (600, 'PYG Paraguayan guaraní'), (634, 'QAR Qatari riyal'), (946, 'RON Romanian leu'), (941, 'RSD Serbian dinar'), (643, 'RUB Russian Federation ruble'), (646, 'RWF Rwandan franc'), (682, 'SAR Saudi riyal'), (90, 'SBD Solomon Islands dollar'), (690, 'SCR Seychelles rupee'), (938, 'SDG Sudanese pound'), (752, 'SEK Swedish krona/kronor'), (702, 'SGD Singapore dollar'), (654, 'SHP Saint Helena pound'), (694, 'SLL Sierra Leonean leone'), (706, 'SOS Somali shilling'), (968, 'SRD Surinamese dollar'), (728, 'SSP South Sudanese pound'), (930, 'STN São Tomé and Príncipe dobra'), (222, 'SVC Salvadoran colón'), (760, 'SYP Syrian pound'), (748, 'SZL Swazi lilangeni'), (764, 'THB Thai baht'), (972, 'TJS Tajikistani somoni'), (934, 'TMT Turkmenistan manat'), (788, 'TND Tunisian dinar'), (776, 'TOP Tongan paʻanga'), (949, 'TRY Turkish lira'), (780, 'TTD Trinidad and Tobago dollar'), (901, 'TWD New Taiwan dollar'), (834, 'TZS Tanzanian shilling'), (980, 'UAH Ukrainian hryvnia'), (800, 'UGX Ugandan shilling'), (840, 'USD United States dollar'), (997, 'USN United States dollar (next day) (funds code)'), (940, 'UYI Uruguay Peso en Unidades Indexadas (URUIURUI) (funds code)'), (858, 'UYU Uruguayan peso'), (860, 'UZS Uzbekistan som'), (937, 'VEF Venezuelan bolívar'), (704, 'VND Vietnamese đồng'), (548, 'VUV Vanuatu vatu'), (882, 'WST Samoan tala'), (950, 'XAF CFA franc BEAC'), (961, 'XAG Silver (one troy ounce)'), (959, 'XAU Gold (one troy ounce)'), (955, 'XBA European Composite Unit (EURCO) (bond market unit)'), (956, 'XBB European Monetary Unit (E.M.U.-6) (bond market unit)'), (957, 'XBC European Unit of Account 9 (E.U.A.-9) (bond market unit)'), (958, 'XBD European Unit of Account 17 (E.U.A.-17) (bond market unit)'), (951, 'XCD East Caribbean dollar'), (960, 'XDR Special drawing rights'), (952, 'XOF CFA franc BCEAO'), (964, 'XPD Palladium (one troy ounce)'), (953, 'XPF CFP franc (franc Pacifique)'), (962, 'XPT Platinum (one troy ounce)'), (994, 'XSU SUCRE'), (963, 'XTS Code reserved for testing purposes'), (965, 'XUA ADB Unit of Account'), (999, 'XXX No currency'), (886, 'YER Yemeni rial'), (710, 'ZAR South African rand'), (967, 'ZMW Zambian kwacha'), (932, 'ZWL Zimbabwean dollar A/10')], db_index=True, verbose_name='Currency')),
                ('value_in_curr', models.DecimalField(blank=True, db_index=True, decimal_places=2, max_digits=14, verbose_name='Value in Currency')),
                ('not_ignore', models.BooleanField(db_index=True, default=True, verbose_name='Do not ignore in statistics and reports')),
                ('bank_date', models.DateField(blank=True, null=True, verbose_name='Transaction Date in Bank')),
                ('bank_ta_id', models.CharField(blank=True, default='', max_length=20, verbose_name='Transaction ID in Bank')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wallet_tag_etc.Category', verbose_name='Category')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wallet_tag_etc.Contact', verbose_name='Contact')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(blank=True, to='wallet_tag_etc.Tag', verbose_name='Tag')),
                ('transfer_related', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='transaction.Transaction')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wallet_tag_etc.Wallet', verbose_name='Wallet')),
            ],
            options={
                'db_table': 'transaction',
                'ordering': ('-date', '-pk'),
            },
        ),
    ]
