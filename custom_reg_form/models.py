from django.conf import settings
from django.db import models


# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True,  related_name='user+', on_delete=models.CASCADE)

    COUNTRIES  = (
                    ('AF' , 'Afghanistan' ),
                    ('AX' , 'Åland Islands' ),
                    ('AL' , 'Albania' ),
                    ('DZ' , 'Algeria' ),
                    ('AS' , 'American Samoa' ),
                    ('AD' , 'Andorra' ),
                    ('AO' , 'Angola' ),
                    ('AI' , 'Anguilla' ),
                    ('AQ' , 'Antarctica' ),
                    ('AG' , 'Antigua and Barbuda' ),
                    ('AR' , 'Argentina' ),
                    ('AM' , 'Armenia' ),
                    ('AW' , 'Aruba' ),
                    ('AU' , 'Australia' ),
                    ('AT' , 'Austria' ),
                    ('AZ' , 'Azerbaijan' ),
                    ('BS' , 'Bahamas' ),
                    ('BH' , 'Bahrain' ),
                    ('BD' , 'Bangladesh' ),
                    ('BB' , 'Barbados' ),
                    ('BY' , 'Belarus' ),
                    ('BE' , 'Belgium' ),
                    ('BZ' , 'Belize' ),
                    ('BJ' , 'Benin' ),
                    ('BM' , 'Bermuda' ),
                    ('BT' , 'Bhutan' ),
                    ('BO' , 'Bolivia' ),
                    ('BA' , 'Bosnia and Herzegovina' ),
                    ('BW' , 'Botswana' ),
                    ('BV' , 'Bouvet Island' ),
                    ('BR' , 'Brazil' ),
                    ('IO' , 'British Indian Ocean Territory' ),
                    ('BN' , 'Brunei Darussalam' ),
                    ('BG' , 'Bulgaria' ),
                    ('BF' , 'Burkina Faso' ),
                    ('BI' , 'Burundi' ),
                    ('KH' , 'Cambodia' ),
                    ('CM' , 'Cameroon' ),
                    ('CA' , 'Canada' ),
                    ('CV' , 'Cape Verde' ),
                    ('KY' , 'Cayman Islands' ),
                    ('CF' , 'Central African Republic' ),
                    ('TD' , 'Chad' ),
                    ('CL' , 'Chile' ),
                    ('CN' , 'China' ),
                    ('CX' , 'Christmas Island' ),
                    ('CC' , 'Cocos  Islands' ),
                    ('CO' , 'Colombia' ),
                    ('KM' , 'Comoros' ),
                    ('CG' , 'Congo' ),
                    ('CD' , 'Congo The Democratic Republic of The' ),
                    ('CK' , 'Cook Islands' ),
                    ('CR' , 'Costa Rica' ),
                    ('CI' , 'Cote D ivoire' ),
                    ('HR' , 'Croatia' ),
                    ('CU' , 'Cuba' ),
                    ('CY' , 'Cyprus' ),
                    ('CZ' , 'Czechia' ),
                    ('DK' , 'Denmark' ),
                    ('DJ' , 'Djibouti' ),
                    ('DM' , 'Dominica' ),
                    ('DO' , 'Dominican Republic' ),
                    ('EC' , 'Ecuador' ),
                    ('EG' , 'Egypt' ),
                    ('SV' , 'El Salvador' ),
                    ('GQ' , 'Equatorial Guinea' ),
                    ('ER' , 'Eritrea' ),
                    ('EE' , 'Estonia' ),
                    ('ET' , 'Ethiopia' ),
                    ('FK' , 'Falkland Islands' ),
                    ('FO' , 'Faroe Islands' ),
                    ('FJ' , 'Fiji' ),
                    ('FI' , 'Finland' ),
                    ('FR' , 'France' ),
                    ('GF' , 'French Guiana' ),
                    ('PF' , 'French Polynesia' ),
                    ('TF' , 'French Southern Territories' ),
                    ('GA' , 'Gabon' ),
                    ('GM' , 'Gambia' ),
                    ('GE' , 'Georgia' ),
                    ('DE' , 'Germany' ),
                    ('GH' , 'Ghana' ),
                    ('GI' , 'Gibraltar' ),
                    ('GR' , 'Greece' ),
                    ('GL' , 'Greenland' ),
                    ('GD' , 'Grenada' ),
                    ('GP' , 'Guadeloupe' ),
                    ('GU' , 'Guam' ),
                    ('GT' , 'Guatemala' ),
                    ('GG' , 'Guernsey' ),
                    ('GN' , 'Guinea' ),
                    ('GW' , 'Guinea-bissau' ),
                    ('GY' , 'Guyana' ),
                    ('HT' , 'Haiti' ),
                    ('HM' , 'Heard Island and Mcdonald Islands' ),
                    ('VA' , 'Vatican City State' ),
                    ('HN' , 'Honduras' ),
                    ('HK' , 'Hong Kong' ),
                    ('HU' , 'Hungary' ),
                    ('IS' , 'Iceland' ),
                    ('IN' , 'India' ),
                    ('ID' , 'Indonesia' ),
                    ('IR' , 'Iran Islamic Republic of' ),
                    ('IQ' , 'Iraq' ),
                    ('IE' , 'Ireland' ),
                    ('IM' , 'Isle of Man' ),
                    ('IL' , 'Israel' ),
                    ('IT' , 'Italy' ),
                    ('JM' , 'Jamaica' ),
                    ('JP' , 'Japan' ),
                    ('JE' , 'Jersey' ),
                    ('JO' , 'Jordan' ),
                    ('KZ' , 'Kazakhstan' ),
                    ('KE' , 'Kenya' ),
                    ('KI' , 'Kiribati' ),
                    ('KP' , 'Korea Democratic Peoples Republic of' ),
                    ('KR' , 'Korea Republic of' ),
                    ('KW' , 'Kuwait' ),
                    ('KG' , 'Kyrgyzstan' ),
                    ('LA' , 'Laos People Democratic Republic' ),
                    ('LV' , 'Latvia' ),
                    ('LB' , 'Lebanon' ),
                    ('LS' , 'Lesotho' ),
                    ('LR' , 'Liberia' ),
                    ('LY' , 'Libyan Arab Jamahiriya' ),
                    ('LI' , 'Liechtenstein' ),
                    ('LT' , 'Lithuania' ),
                    ('LU' , 'Luxembourg' ),
                    ('MO' , 'Macao' ),
                    ('MK' , 'Macedonia The Former Yugoslav Republic of' ),
                    ('MG' , 'Madagascar' ),
                    ('MW' , 'Malawi' ),
                    ('MY' , 'Malaysia' ),
                    ('MV' , 'Maldives' ),
                    ('ML' , 'Mali' ),
                    ('MT' , 'Malta' ),
                    ('MH' , 'Marshall Islands' ),
                    ('MQ' , 'Martinique' ),
                    ('MR' , 'Mauritania' ),
                    ('MU' , 'Mauritius' ),
                    ('YT' , 'Mayotte' ),
                    ('MX' , 'Mexico' ),
                    ('FM' , 'Micronesia' ),
                    ('MD' , 'Moldova' ),
                    ('MC' , 'Monaco' ),
                    ('MN' , 'Mongolia' ),
                    ('ME' , 'Montenegro' ),
                    ('MS' , 'Montserrat' ),
                    ('MA' , 'Morocco' ),
                    ('MZ' , 'Mozambique' ),
                    ('MM' , 'Myanmar' ),
                    ('NA' , 'Namibia' ),
                    ('NR' , 'Nauru' ),
                    ('NP' , 'Nepal' ),
                    ('NL' , 'Netherlands' ),
                    ('AN' , 'Netherlands Antilles' ),
                    ('NC' , 'New Caledonia' ),
                    ('NZ' , 'New Zealand' ),
                    ('NI' , 'Nicaragua' ),
                    ('NE' , 'Niger' ),
                    ('NG' , 'Nigeria' ),
                    ('NU' , 'Niue' ),
                    ('NF' , 'Norfolk Island' ),
                    ('MP' , 'Northern Mariana Islands' ),
                    ('NO' , 'Norway' ),
                    ('OM' , 'Oman' ),
                    ('PK' , 'Pakistan' ),
                    ('PW' , 'Palau' ),
                    ('PS' , 'Palestinian Territory Occupied' ),
                    ('PA' , 'Panama' ),
                    ('PG' , 'Papua New Guinea' ),
                    ('PY' , 'Paraguay' ),
                    ('PE' , 'Peru' ),
                    ('PH' , 'Philippines' ),
                    ('PN' , 'Pitcairn' ),
                    ('PL' , 'Poland' ),
                    ('PT' , 'Portugal' ),
                    ('PR' , 'Puerto Rico' ),
                    ('QA' , 'Qatar' ),
                    ('RE' , 'Reunion' ),
                    ('RO' , 'Romania' ),
                    ('RU' , 'Russian Federation' ),
                    ('RW' , 'Rwanda' ),
                    ('SH' , 'Saint Helena' ),
                    ('KN' , 'Saint Kitts and Nevis' ),
                    ('LC' , 'Saint Lucia' ),
                    ('PM' , 'Saint Pierre and Miquelon' ),
                    ('VC' , 'Saint Vincent and The Grenadines' ),
                    ('WS' , 'Samoa' ),
                    ('SM' , 'San Marino' ),
                    ('ST' , 'Sao Tome and Principe' ),
                    ('SA' , 'Saudi Arabia' ),
                    ('SN' , 'Senegal' ),
                    ('RS' , 'Serbia' ),
                    ('SC' , 'Seychelles' ),
                    ('SL' , 'Sierra Leone' ),
                    ('SG' , 'Singapore' ),
                    ('SK' , 'Slovakia' ),
                    ('SI' , 'Slovenia' ),
                    ('SB' , 'Solomon Islands' ),
                    ('SO' , 'Somalia' ),
                    ('ZA' , 'South Africa' ),
                    ('GS' , 'South Georgia and The South Sandwich Islands' ),
                    ('ES' , 'Spain' ),
                    ('LK' , 'Sri Lanka' ),
                    ('SD' , 'Sudan' ),
                    ('SR' , 'Suriname' ),
                    ('SJ' , 'Svalbard and Jan Mayen' ),
                    ('SZ' , 'Swaziland' ),
                    ('SE' , 'Sweden' ),
                    ('CH' , 'Switzerland' ),
                    ('SY' , 'Syrian Arab Republic' ),
                    ('TW' , 'Taiwan Province of China' ),
                    ('TJ' , 'Tajikistan' ),
                    ('TZ' , 'Tanzania United Republic of' ),
                    ('TH' , 'Thailand' ),
                    ('TL' , 'Timor-leste' ),
                    ('TG' , 'Togo' ),
                    ('TK' , 'Tokelau' ),
                    ('TO' , 'Tonga' ),
                    ('TT' , 'Trinidad and Tobago' ),
                    ('TN' , 'Tunisia' ),
                    ('TR' , 'Turkey' ),
                    ('TM' , 'Turkmenistan' ),
                    ('TC' , 'Turks and Caicos Islands' ),
                    ('TV' , 'Tuvalu' ),
                    ('UG' , 'Uganda' ),
                    ('UA' , 'Ukraine' ),
                    ('AE' , 'United Arab Emirates' ),
                    ('GB' , 'United Kingdom' ),
                    ('US' , 'United States' ),
                    ('UM' , 'United States Minor Outlying Islands' ),
                    ('UY' , 'Uruguay' ),
                    ('UZ' , 'Uzbekistan' ),
                    ('VU' , 'Vanuatu' ),
                    ('VE' , 'Venezuela' ),
                    ('VN' , 'Viet Nam' ),
                    ('VG' , 'Virgin Islands British' ),
                    ('VI' , 'Virgin Islands US' ),
                    ('WF' , 'Wallis and Futuna' ),
                    ('EH' , 'Western Sahara' ),
                    ('YE' , 'Yemen' ),
                    ('ZM' , 'Zambia' ),
                    ('ZW' , 'Zimbabwe'), 
                    )

    
     
    
    
    nationality = models.CharField(
        verbose_name="Nationality",
        choices=COUNTRIES,
        blank=True,
        max_length=100,
    )
    
    age = models.CharField(
        verbose_name="Age",
        max_length=20,
    )

    phone_number = models.CharField(
        verbose_name="Phone Number",
        max_length=100,
    )    
    
    
    def __str__(self):
        result = '{0.user} {0.nationality} {0.age} {0.phone_number}'
        return result.format(self)



