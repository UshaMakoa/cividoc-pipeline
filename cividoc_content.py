"""Configuration éditoriale déclarative du pipeline CiviDoc.

Ce module constitue la source unique des taxonomies, libellés, catalogues et
prompts. Il ne contient aucune opération de pipeline.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

PIPELINE_VERSION = '2026.10-diataxis-v8'
NAVIGATION_PROMPT_VERSION = 'diataxis-semantic-nav-v8'
REWRITE_PROMPT_VERSION = 'diataxis-split-v8'
DEFAULT_WORKSPACE = '.cividoc'
DEFAULT_OUTPUT = 'generated-civicrm-docs'
DEFAULT_GUIDES = 'user-en,installation,sysadmin'
DEFAULT_FIDELITY_ATTEMPTS = 3

BROWSE_DIR = "_browse"
MAX_NAV_CHOICES = 18
MAX_MAIN_ROOT_CHOICES = 6
MAX_NAV_DEPTH = 3

ALLOWED_CATEGORIES = {'how-to', 'tutorial', 'explanation', 'reference'}
ALLOWED_LEVELS = {'intermediate', 'basic', 'advanced'}
CATEGORY_LABELS = {'tutorial': 'Tutorials',
 'how-to': 'How-to guides',
 'reference': 'Reference',
 'explanation': 'Explanation'}
CATEGORY_ALIASES = {'tutorial': 'tutorial',
 'tutorials': 'tutorial',
 'learning': 'tutorial',
 'how-to': 'how-to',
 'howto': 'how-to',
 'how-to-guide': 'how-to',
 'how-to-guides': 'how-to',
 'explanation': 'explanation',
 'explanations': 'explanation',
 'concept': 'explanation',
 'concepts': 'explanation',
 'reference': 'reference',
 'references': 'reference'}

TOPIC_DEFINITIONS: Dict[str, Dict[str, Any]] = {'contacts': {'label': 'Contacts',
              'domain': 'Contacts and data',
              'component': 'CiviCRM Core',
              'aliases': (),
              'keywords': ('contact', 'individual', 'household', 'organization')},
 'activities': {'label': 'Activities',
                'domain': 'Contacts and data',
                'component': 'CiviCRM Core',
                'aliases': (),
                'keywords': ('activity', 'activities')},
 'groups-and-tags': {'label': 'Groups and tags',
                     'domain': 'Contacts and data',
                     'component': 'CiviCRM Core',
                     'aliases': (),
                     'keywords': ('group', 'tag')},
 'data-management': {'label': 'Data management',
                     'domain': 'Contacts and data',
                     'component': 'CiviCRM Core',
                     'aliases': (),
                     'keywords': ('import', 'export', 'dedup', 'merge', 'undelete', 'trash')},
 'communication': {'label': 'Communication',
                   'domain': 'Communication',
                   'component': 'CiviCRM Core',
                   'aliases': (),
                   'keywords': ()},
 'mailings': {'label': 'Mailings',
              'domain': 'Communication',
              'component': 'CiviMail',
              'aliases': ('civimail', 'mailing', 'email'),
              'keywords': ('mailing', 'civimail', 'email')},
 'campaigns': {'label': 'Campaigns',
               'domain': 'Communication',
               'component': 'CiviCampaign',
               'aliases': ('civicampaign',),
               'keywords': ('campaign', 'civicampaign', 'survey', 'petition')},
 'contributions': {'label': 'Contributions',
                   'domain': 'Fundraising and engagement',
                   'component': 'CiviContribute',
                   'aliases': ('civicontribute', 'donations', 'payments'),
                   'keywords': ('contribution', 'payment', 'civicontribute', 'financial')},
 'events': {'label': 'Events',
            'domain': 'Fundraising and engagement',
            'component': 'CiviEvent',
            'aliases': ('civievent',),
            'keywords': ('event', 'participant', 'civievent')},
 'memberships': {'label': 'Memberships',
                 'domain': 'Fundraising and engagement',
                 'component': 'CiviMember',
                 'aliases': ('civimember',),
                 'keywords': ('membership', 'civimember')},
 'cases': {'label': 'Cases',
           'domain': 'Fundraising and engagement',
           'component': 'CiviCase',
           'aliases': ('civicase',),
           'keywords': ('case', 'civicase')},
 'grants': {'label': 'Grants',
            'domain': 'Fundraising and engagement',
            'component': 'CiviGrant',
            'aliases': ('civigrant',),
            'keywords': ('grant', 'civigrant')},
 'pledges': {'label': 'Pledges',
             'domain': 'Fundraising and engagement',
             'component': 'CiviContribute',
             'aliases': (),
             'keywords': ('pledge',)},
 'search': {'label': 'Search',
            'domain': 'Search and reporting',
            'component': 'CiviCRM Core',
            'aliases': (),
            'keywords': ('search', 'find ')},
 'reporting': {'label': 'Reporting',
               'domain': 'Search and reporting',
               'component': 'CiviReport',
               'aliases': ('reports',),
               'keywords': ('report', 'dashboard')},
 'searchkit': {'label': 'SearchKit',
               'domain': 'Search and reporting',
               'component': 'SearchKit',
               'aliases': (),
               'keywords': ('searchkit', 'formbuilder', 'form builder')},
 'forms': {'label': 'Forms',
           'domain': 'Search and reporting',
           'component': 'FormBuilder',
           'aliases': ('form-builder', 'formbuilder'),
           'keywords': ('form',)},
 'configuration': {'label': 'Configuration',
                   'domain': 'Configure, automate and extend',
                   'component': 'CiviCRM Core',
                   'aliases': (),
                   'keywords': ('configuration', 'configure', 'setting')},
 'permissions': {'label': 'Permissions',
                 'domain': 'Configure, automate and extend',
                 'component': 'CiviCRM Core',
                 'aliases': (),
                 'keywords': ('permission', 'access control', 'acl')},
 'custom-data': {'label': 'Custom data',
                 'domain': 'Configure, automate and extend',
                 'component': 'CiviCRM Core',
                 'aliases': ('custom-fields',),
                 'keywords': ('custom field', 'custom data', 'profile')},
 'installation': {'label': 'Installation',
                  'domain': 'Configure, automate and extend',
                  'component': 'CiviCRM Core',
                  'aliases': (),
                  'keywords': ()},
 'system-administration': {'label': 'System administration',
                           'domain': 'Configure, automate and extend',
                           'component': 'CiviCRM Core',
                           'aliases': ('administration', 'sysadmin'),
                           'keywords': ()},
 'extensions': {'label': 'Extensions',
                'domain': 'Configure, automate and extend',
                'component': 'CiviCRM Extensions',
                'aliases': (),
                'keywords': ('extension',)},
 'troubleshooting': {'label': 'Troubleshooting',
                     'domain': 'Configure, automate and extend',
                     'component': 'CiviCRM Core',
                     'aliases': (),
                     'keywords': ('troubleshoot', 'error', 'debug')},
 'general': {'label': 'General',
             'domain': 'Configure, automate and extend',
             'component': 'CiviCRM Core',
             'aliases': ('civicrm', 'core', 'civicrm-core'),
             'keywords': ()}}
TOPIC_LABELS = {key: value["label"] for key, value in TOPIC_DEFINITIONS.items()}
TOPIC_DOMAIN = {key: value["domain"] for key, value in TOPIC_DEFINITIONS.items()}
COMPONENT_BY_TOPIC = {key: value["component"] for key, value in TOPIC_DEFINITIONS.items()}
TOPIC_KEYWORDS = {key: tuple(value["keywords"]) for key, value in TOPIC_DEFINITIONS.items()}
TOPIC_ALIASES = {
    alias: topic
    for topic, definition in TOPIC_DEFINITIONS.items()
    for alias in (topic, *definition["aliases"])
}
ALLOWED_TOPICS = frozenset(TOPIC_DEFINITIONS)
DOMAIN_ORDER = ['Contacts and data',
 'Communication',
 'Fundraising and engagement',
 'Search and reporting',
 'Configure, automate and extend']

JOURNEY_STAGE_DEFINITIONS: Dict[str, Dict[str, Any]] = {'overview': {'label': 'Overview',
              'aliases': ('discover', 'understand'),
              'keywords': ('what is ', 'overview', 'introduction', 'concept')},
 'plan-and-configure': {'label': 'Plan and configure',
                        'aliases': ('prepare', 'configure'),
                        'keywords': ('configure',
                                     'configuration',
                                     'setup',
                                     'set up',
                                     'plan',
                                     'template',
                                     'option')},
 'everyday-tasks': {'label': 'Everyday tasks', 'aliases': ('use', 'operate'), 'keywords': ()},
 'manage-and-automate': {'label': 'Manage and automate',
                         'aliases': ('manage', 'automate'),
                         'keywords': ('bulk',
                                      'batch',
                                      'automate',
                                      'scheduled',
                                      'workflow',
                                      'manage')},
 'reports-and-review': {'label': 'Reports and review',
                        'aliases': ('review', 'report'),
                        'keywords': ('report', 'search', 'review', 'find ', 'dashboard')},
 'reference-and-troubleshooting': {'label': 'Reference and troubleshooting',
                                   'aliases': ('resolve', 'troubleshoot'),
                                   'keywords': ('troubleshoot',
                                                'error',
                                                'status',
                                                'permission',
                                                'reference')},
 'extensions-and-integrations': {'label': 'Extensions and integrations',
                                 'aliases': ('integrate',),
                                 'keywords': ('extension', 'integration', 'integrate')}}
STAGE_LABELS = {key: value["label"] for key, value in JOURNEY_STAGE_DEFINITIONS.items()}
STAGE_ORDER = {stage: index for index, stage in enumerate(STAGE_LABELS)}
JOURNEY_STAGE_ALIASES = {
    alias: stage
    for stage, definition in JOURNEY_STAGE_DEFINITIONS.items()
    for alias in (stage, *definition["aliases"])
}
JOURNEY_STAGE_KEYWORDS = {key: tuple(value["keywords"]) for key, value in JOURNEY_STAGE_DEFINITIONS.items()}
ALLOWED_JOURNEY_STAGES = frozenset(JOURNEY_STAGE_DEFINITIONS)

AUDIENCE_LABELS = {'decision-maker': 'Decision makers',
 'civicrm-user': 'CiviCRM users',
 'functional-administrator': 'Functional administrators',
 'data-and-reporting-specialist': 'Data and reporting specialists',
 'system-administrator': 'System administrators',
 'implementer': 'Implementers and site builders',
 'developer': 'Developers',
 'documentation-contributor': 'Documentation contributors'}
AUDIENCE_ALIASES = {'decision-maker': 'decision-maker',
 'decision-makers': 'decision-maker',
 'organisation-decision-maker': 'decision-maker',
 'organisation-decision-makers': 'decision-maker',
 'organizational-decision-maker': 'decision-maker',
 'organizational-decision-makers': 'decision-maker',
 'organisations-planning-to-use-civicrm': 'decision-maker',
 'prospective-user': 'decision-maker',
 'prospective-users': 'decision-maker',
 'civicrm-user': 'civicrm-user',
 'civicrm-users': 'civicrm-user',
 'user': 'civicrm-user',
 'users': 'civicrm-user',
 'staff': 'civicrm-user',
 'internal-user': 'civicrm-user',
 'internal-users': 'civicrm-user',
 'office-staff': 'civicrm-user',
 'nonprofit-staff': 'civicrm-user',
 'non-profit-staff': 'civicrm-user',
 'volunteer': 'civicrm-user',
 'volunteers': 'civicrm-user',
 'functional-administrator': 'functional-administrator',
 'functional-administrators': 'functional-administrator',
 'power-user': 'functional-administrator',
 'power-users': 'functional-administrator',
 'form-builder': 'functional-administrator',
 'form-builders': 'functional-administrator',
 'data-and-reporting-specialist': 'data-and-reporting-specialist',
 'data-importer': 'data-and-reporting-specialist',
 'data-importers': 'data-and-reporting-specialist',
 'report-user': 'data-and-reporting-specialist',
 'report-users': 'data-and-reporting-specialist',
 'report-builder': 'data-and-reporting-specialist',
 'report-builders': 'data-and-reporting-specialist',
 'search-builder': 'data-and-reporting-specialist',
 'search-builders': 'data-and-reporting-specialist',
 'searchkit-user': 'data-and-reporting-specialist',
 'searchkit-users': 'data-and-reporting-specialist',
 'search-kit-user': 'data-and-reporting-specialist',
 'search-kit-users': 'data-and-reporting-specialist',
 'system-administrator': 'system-administrator',
 'system-administrators': 'system-administrator',
 'site-administrator': 'system-administrator',
 'site-administrators': 'system-administrator',
 'website-administrator': 'system-administrator',
 'website-administrators': 'system-administrator',
 'technical-user': 'system-administrator',
 'technical-users': 'system-administrator',
 'technician': 'system-administrator',
 'technicians': 'system-administrator',
 'people-installing-civicrm': 'system-administrator',
 'implementer': 'implementer',
 'implementers': 'implementer',
 'site-builder': 'implementer',
 'site-builders': 'implementer',
 'civicrm-site-builder': 'implementer',
 'civicrm-site-builders': 'implementer',
 'project-manager': 'implementer',
 'project-managers': 'implementer',
 'developer': 'developer',
 'developers': 'developer',
 'civicrm-developer': 'developer',
 'civicrm-developers': 'developer',
 'documentation-contributor': 'documentation-contributor',
 'documentation-contributors': 'documentation-contributor',
 'community-contributor': 'documentation-contributor',
 'community-contributors': 'documentation-contributor'}
AUDIENCE_KEYWORDS = [('developer', ('developer', 'development', 'api', 'programmer', 'code')),
 ('documentation-contributor', ('documentation', 'manual', 'contributor')),
 ('system-administrator',
  ('system administrator',
   'site administrator',
   'website administrator',
   'technical',
   'technician',
   'install')),
 ('data-and-reporting-specialist',
  ('report', 'search', 'searchkit', 'data import', 'data export', 'analyst')),
 ('implementer',
  ('implementer', 'site builder', 'project manager', 'configure profiles', 'planning data')),
 ('functional-administrator',
  ('administrator', 'manager', 'organizer', 'organiser', 'builder', 'power user')),
 ('decision-maker', ('decision maker', 'planning to use', 'prospective')),
 ('civicrm-user', ('user', 'staff', 'volunteer', 'author', 'worker'))]

AUDIENCE_DEFINITIONS = {
    "newcomer": {
        "label": "Newcomers",
        "keywords": (
            "getting started",
            "introduction",
            "first steps",
            "overview",
            "what is",
        ),
    },
    "operations-user": {
        "label": "Operations users",
        "keywords": (
            "contact",
            "activity",
            "case",
            "grant",
            "search",
            "report",
            "import",
            "export",
        ),
    },
    "fundraising-manager": {
        "label": "Fundraising managers",
        "keywords": (
            "contribution",
            "donation",
            "fundraising",
            "pledge",
            "payment",
            "soft credit",
        ),
    },
    "membership-manager": {
        "label": "Membership managers",
        "keywords": (
            "membership",
            "member",
            "renewal",
        ),
    },
    "event-manager": {
        "label": "Event managers",
        "keywords": (
            "event",
            "participant",
            "registration",
            "attendee",
        ),
    },
    "communications-manager": {
        "label": "Communications managers",
        "keywords": (
            "mailing",
            "newsletter",
            "civimail",
            "sms",
            "campaign",
            "message template",
        ),
    },
    "administrator": {
        "label": "CiviCRM administrators",
        "keywords": (
            "configure",
            "configuration",
            "setting",
            "permission",
            "acl",
            "profile",
            "custom field",
            "formbuilder",
            "scheduled job",
        ),
    },
    "technical": {
        "label": "Technical teams",
        "keywords": (
            "install",
            "upgrade",
            "server",
            "backup",
            "security",
            "cron",
            "api",
            "developer",
            "extension",
            "hook",
            "integration",
        ),
    },
}

ALLOWED_AUDIENCES = frozenset(
    AUDIENCE_DEFINITIONS
)
    
CURATED_EXTENSIONS_START = "<!-- cividoc:popular-extensions:start -->"
CURATED_EXTENSIONS_END = "<!-- cividoc:popular-extensions:end -->"
CURATED_EXTENSIONS_REVIEWED_ON = "2026-10-13"
EXTENSION_CATALOG_BY_COMPONENT: Dict[str, Dict[str, Any]] = {'CiviMail': {'category_id': 95,
              'items': [('Mosaico CiviCRM Integration', 'email-template-builder', 4729),
                        ('E-mail API', 'e-mail-api', 3072),
                        ('Fuzion Tokens', 'fuzion-tokens', 1489),
                        ('PDF Creation API', 'pdf-creation-api', 438),
                        ('Mosaico Tweaks', 'mosaico-tweaks', 253)]},
 'CiviCampaign': {'category_id': 100,
                  'items': [('Campaign Manager', 'campaign-manager', 102),
                            ('Campaign Tools', 'campaign-tools', 15),
                            ('CiviRepresent', 'civirepresent', 11),
                            ('Petition Email', 'petition-email', 10)]},
 'CiviContribute': {'category_id': 94,
                    'items': [('CiviSEPA — SEPA Direct Debit Extension',
                               'civisepa-sepa-direct-debit-extension',
                               925),
                              ('no overwrite', 'no-overwrite', 918),
                              ('Summary Fields', 'summary-fields', 663),
                              ('Line Item Editor', 'line-item-editor', 565),
                              ('Percentage Price Field', 'percentage-price-field', 385)]},
 'CiviEvent': {'category_id': 98,
               'items': [('CiviDiscount', 'cividiscount', 1834),
                         ('no overwrite', 'no-overwrite', 918),
                         ('Summary Fields', 'summary-fields', 663),
                         ('Line Item Editor', 'line-item-editor', 565),
                         ('CiviMobileAPI', 'civimobileapi', 406)]},
 'CiviMember': {'category_id': 97,
                'items': [('CiviDiscount', 'cividiscount', 1834),
                          ('Fuzion Tokens', 'fuzion-tokens', 1489),
                          ('Line Item Editor', 'line-item-editor', 565),
                          ('Percentage Price Field', 'percentage-price-field', 385),
                          ('Membership Extras', 'membership-extras', 295)]},
 'CiviCase': {'category_id': 99,
              'items': [('Documents', 'documents', 337),
                        ('CiviCalendar', 'civicalendar', 250),
                        ('New CiviCase UI', 'civicase-v5', 206),
                        ('CiviProspect', 'civiprospect', 176),
                        ('CiviCase Tokens', 'civicase-tokens', 123)]},
 'CiviGrant': {'category_id': 101,
               'items': [('Grant Application Pages', 'grant-application-pages', 62),
                         ('CiviGantt', 'civigantt', 7),
                         ('Batch Update of Grants via Profile', 'batch-update-grants-profile', 6),
                         ('Grant Prefill', 'grant-prefill', 2),
                         ('Print Grant PDFs', 'print-grant-pdfs', 2)]},
 'CiviReport': {'category_id': 126,
                'items': [('Extended Reports', 'extended-reports', 2399),
                          ('SearchKit Tokens', 'searchkit-tokens', 1733),
                          ('Chart Kit', 'chart-kit', 1187),
                          ('Export to native Excel', 'export-native-excel', 959),
                          ('Civisualize',
                           'civisualize-missing-data-visualization-extension',
                           718)]},
 'SearchKit': {'category_id': 126,
               'items': [('Extended Reports', 'extended-reports', 2399),
                         ('SearchKit Tokens', 'searchkit-tokens', 1733),
                         ('Chart Kit', 'chart-kit', 1187),
                         ('Export to native Excel', 'export-native-excel', 959),
                         ('Civisualize', 'civisualize-missing-data-visualization-extension', 718)]},
 'FormBuilder': {'category_id': 214,
                 'items': [('Extended Contact Matcher (XCM)', 'extended-contact-matcher-xcm', 1089),
                           ('Action Provider', 'action-provider', 898),
                           ('Mailchimp CiviCRM Integration', 'mailchimp-civicrm-integration', 818),
                           ('Form Processor', 'form-processor', 716),
                           ('Data Processor', 'data-processor', 551)]},
 'CiviCRM Core': {'category_id': 385,
                  'items': [('API csv Import GUI', 'api-csv-import-gui', 1678),
                            ('Advanced Import', 'advanced-import', 292),
                            ('Option Value Importer', 'option-value-importer', 71),
                            ('CSV Import Helper', '../node/5879', 69),
                            ('Advanced Import Form Processor',
                             'advanced-import-form-processor',
                             58)]},
 'CiviCRM Extensions': {'category_id': 214,
                        'items': [('Extended Contact Matcher (XCM)',
                                   'extended-contact-matcher-xcm',
                                   1089),
                                  ('Action Provider', 'action-provider', 898),
                                  ('Mailchimp CiviCRM Integration',
                                   'mailchimp-civicrm-integration',
                                   818),
                                  ('Form Processor', 'form-processor', 716),
                                  ('Data Processor', 'data-processor', 551)]}}

@dataclass(frozen=True)
class GuideConfig:
    key: str
    repository: str
    public_slug: str
    destination_prefix: str
    label: str

GUIDES: Dict[str, GuideConfig] = {
    "user-en": GuideConfig("user-en", "https://lab.civicrm.org/documentation/docs/user-en.git", "user", "", "User guide"),
    "installation": GuideConfig("installation", "https://lab.civicrm.org/documentation/docs/installation.git", "installation", "installation", "Installation guide"),
    "sysadmin": GuideConfig("sysadmin", "https://lab.civicrm.org/documentation/docs/sysadmin.git", "sysadmin", "sysadmin", "System administrator guide"),
}

REWRITE_PROMPT = '\nYou are editing official CiviCRM documentation. Rewrite the supplied Markdown\nonly when doing so improves structure, clarity, findability, or Diátaxis focus.\n\nSOURCE AUTHORITY\n- The supplied source page is the only authority on how CiviCRM works.\n- Do not invent steps, options, facts, prerequisites, warnings, interface\n  behaviour, links, extension recommendations, or compatibility claims.\n- Preserve every source step, option, limitation, warning, example, table,\n  image, anchor, code block, meaningful link, menu path, field name, button\n  label, command, configuration key, placeholder, literal, and URL.\n- If the source is unclear, contradictory, or apparently outdated, preserve it\n  and describe the concern in review_notes instead of silently correcting it.\n\nDIATAXIS PURPOSE\nClassify each output page as exactly one of:\n- tutorial: a guided learning experience with a meaningful outcome;\n- how-to: directions for completing one concrete real-world task;\n- reference: accurate lookup information such as fields, settings, commands,\n  permissions, statuses, requirements, APIs, tables, or exhaustive lists;\n- explanation: concepts, architecture, context, relationships, rationale,\n  lifecycle, planning, or trade-offs.\n\nCLASSIFICATION RULES\n- Worked examples, quick starts, and end-to-end guided first experiences are\n  normally tutorials, even when they contain numbered steps.\n- Imperative procedures for an already oriented reader are normally how-to\n  guides.\n- "What is ...?", conceptual overview, architecture, and planning pages are\n  normally explanations.\n- Do not classify a page as reference merely because it lacks numbered steps.\n- Classify every split output independently from its own purpose.\n\nLONG-PAGE POLICY\n- Measure reader purpose, not file size alone.\n- Consider splitting a source with more than about 1,800 prose words, more than\n  eight substantial H2 sections, or several clearly independent user goals.\n- Split only at a genuine purpose or task boundary. Do not split a coherent\n  procedure, tutorial, table, code sample, warning, or short fragment.\n- Aim for focused pages that usually contain about 700-1,600 prose words, but\n  fidelity and task completeness take priority over that range.\n- A mixed page may become, for example, an explanation plus one or more how-to\n  guides and a reference page. Never force all outputs into one category.\n- Additional pages must have specific semantic titles. Never use Part 1,\n  Part 2, Continued, More, General, or Basic as a page title.\n- Separate complete output pages with exactly: === NEW PAGE ===\n- The first output keeps the source path and official URL. Additional outputs\n  are generated sibling pages.\n\nFRONT MATTER\nStart every page at its first character with this YAML schema:\n---\ntitle: Clear, specific page title\ncategory: tutorial|how-to|reference|explanation\ntopic: stable-functional-topic\nsubtopic: precise-semantic-subgroup\ncomponent: CiviCRM component or feature\naudiences:\n  - primary-reader\nlevel: basic|intermediate|advanced\njourney_stage: overview|plan-and-configure|everyday-tasks|manage-and-automate|reports-and-review|reference-and-troubleshooting|extensions-and-integrations\nsummary: One sentence describing the page benefit.\nextensions: []\nrelated: []\nreview_priority: low|medium|high\nreview_notes: []\n---\n\nMETADATA\n- Use one canonical functional topic and a precise subtopic; never use General\n  when a meaningful task or feature label can be derived from the source.\n- Use only these audience ids: decision-maker, civicrm-user,\n  functional-administrator, data-and-reporting-specialist,\n  system-administrator, implementer, developer, documentation-contributor.\n- Assign one primary audience and at most one secondary audience.\n- Event manager, fundraiser, campaign organiser, mailing author, and similar\n  jobs are topics or subtopics, not audience ids.\n- Use extensions only when the source explicitly identifies an extension.\n- Use related only for source paths or links supported by the source.\n- Preserve a "What is CiviX?" title as that component\'s explanation entry page.\n\nWRITING\n- Write clear, inclusive, professional English.\n- Preserve one H1 and use sentence case headings.\n- Preserve explicit heading IDs. When renaming a heading, add its old anchor.\n- Keep paragraphs short and use numbered lists only when order matters.\n- Do not add filler, marketing claims, or repetitive conclusions.\n- End each output with exactly one source comment using the supplied path.\n- Return Markdown only, without an outer code fence.\n'
FIDELITY_CORRECTION_PROMPT = '\nCORRECTION REQUIRED\n\nYour previous response failed source-fidelity validation:\n\n{error}\n\nGenerate the complete page again. Restore every missing source element exactly,\nespecially Markdown link targets, image references, warnings, limitations, code\nblocks, inline code, anchors, menu paths, field names, button labels,\nconfiguration values, placeholders, and technical literals.\n\nDo not explain the correction. Return only the complete rewritten Markdown.\n'
NAVIGATION_PROMPT = """
You are the information architect for a unified CiviCRM documentation site.

You receive a complete page inventory. Every page has an immutable opaque id
and metadata describing category, topic, subtopic, audiences, level,
journey stage and component.

OUTPUT
Return JSON only in this exact form:

{"nav": [...]}

Use only these node types:
- section: {"title": "...", "children": [...]}
- page: {"page_id": "p00001"}

INTEGRITY
- Use every page_id exactly once.
- Copy every page_id exactly.
- Never invent, omit or repeat an id.
- Treat sibling titles case-insensitively when checking duplicates.
- Do not create empty sections.
- Do not create a section containing only one page.
- Flatten redundant section -> section -> page chains.

PRIMARY ARCHITECTURE
The main navigation must be functional: organise pages according to what
people need to do with CiviCRM.

Do not use Diátaxis categories, audiences, levels or journey stages as the
primary hierarchy. They are transverse metadata and browse indexes.

Use no more than six root sections, following this functional model:

1. Getting started
2. Daily work
3. Configure CiviCRM
4. Maintain and operate
5. Develop and integrate

FUNCTIONAL SEPARATION
- Getting started: discovery, concepts needed by newcomers, first steps and
  guided introductory tutorials.
- Daily work: recurring operational tasks performed by staff, including
  contacts, contributions, memberships, events, mailings, campaigns,
  searches and reports.
- Configure CiviCRM: administrative and functional configuration, including
  permissions, payment processors, profiles, custom fields, forms,
  workflows and organisation settings.
- Maintain and operate: installation, upgrades, backups, scheduled jobs,
  security, performance, infrastructure and troubleshooting.
- Develop and integrate: APIs, hooks, extensions, integrations and
  developer reference.

Never mix:
- installation or upgrades with routine user tasks;
- administrative configuration with daily data entry;
- developer implementation with end-user procedures.

DIATAXIS
Every page keeps exactly one category:
- tutorial;
- how-to;
- reference;
- explanation.

Use the category to improve placement and grouping, but do not create a
Diátaxis subtree under every component.

- Tutorials provide guided learning experiences.
- How-to guides help competent readers complete real tasks.
- Reference pages describe facts, fields, options or system behaviour.
- Explanation pages provide context, concepts and reasons.

Diátaxis category pages are generated separately under Browse documentation.
Journey stage controls ordering but is not a mandatory folder structure.
Audiences and levels are browse metadata, never primary navigation branches.

DEPTH AND DENSITY
- Use at most six root choices; Browse is added later by the pipeline.
- Prefer root -> functional domain -> page.
- Allow one additional semantic subgroup only when genuinely necessary.
- Never require more than three section levels before a page.
- Use no more than eighteen direct choices in a section.
- Prefer five to nine choices per menu.
- Keep small components flat.
- Create subgroups only when each subgroup has at least two children.
- Avoid excessive menus and redundant wrappers.

LABELS
Use precise functional labels derived from the inventory.

Never use:
- General;
- Miscellaneous;
- Other;
- More;
- Continued;
- alphabetical buckets;
- numbered continuations;
- guide or repository names.

ACCESSIBLE TERMINOLOGY
- Write navigation labels for readers who do not yet know CiviCRM terminology.
- Prefer "Fundraising, donations and payments" to a bare "Contributions".
- Prefer "People and organisations" to a bare "Contacts" when introducing
  the concept.
- Prefer "Email, SMS and communications" to product-only labels.
- Prefer "Search, lists and reports" to technical query terminology.
- Keep official CiviCRM terms in individual page titles where required.
- When the official term "contribution" is necessary, introduce it as the
  CiviCRM umbrella term for donations, membership payments, event fees,
  other payments and in-kind gifts.

QUALITY CHECK
Before returning the result, verify that:
- installation is separated from daily user work;
- configuration is separated from recurring operations;
- developers have a clearly identifiable area;
- every page_id occurs exactly once;
- no singleton or empty section remains;
- no sibling labels collide case-insensitively;
- the result follows the exact {"nav": [...]} schema.

Return JSON only.
"""

INDEX_PAGES_CSS = r"""
.md-typeset .cividoc-category-list,
.md-typeset .cividoc-audience-list {
  margin-block: 1.5rem 2rem;
}

.md-typeset .cividoc-category-list ul,
.md-typeset .cividoc-audience-list ul {
  display: grid;
  grid-template-columns: repeat(
    auto-fit,
    minmax(min(100%, 21rem), 1fr)
  );
  gap: 1rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.md-typeset .cividoc-category-list li,
.md-typeset .cividoc-audience-list li {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  min-width: 0;
  margin: 0;
  padding: 1rem 1.1rem;
  border: 1px solid
    color-mix(
      in srgb,
      var(--md-default-fg-color) 14%,
      transparent
    );
  border-radius: 0.5rem;
  background: var(--md-default-bg-color);
  box-shadow: 0 1px 2px rgb(0 0 0 / 4%);
  transition:
    border-color 150ms ease,
    box-shadow 150ms ease,
    transform 150ms ease;
}

.md-typeset .cividoc-category-list li:hover,
.md-typeset .cividoc-audience-list li:hover {
  border-color:
    color-mix(
      in srgb,
      var(--md-accent-fg-color) 45%,
      transparent
    );
  box-shadow: 0 0.3rem 0.9rem rgb(0 0 0 / 8%);
  transform: translateY(-1px);
}

.md-typeset .cividoc-category-list li > a,
.md-typeset .cividoc-audience-list li > a {
  color: var(--md-typeset-a-color);
  font-size: 0.95rem;
  line-height: 1.35;
  text-decoration: none;
}

.md-typeset .cividoc-category-list li > a:hover,
.md-typeset .cividoc-audience-list li > a:hover {
  color: var(--md-accent-fg-color);
  text-decoration: underline;
  text-underline-offset: 0.15em;
}

.md-typeset .cividoc-category-list li > a:focus-visible,
.md-typeset .cividoc-audience-list li > a:focus-visible {
  outline: 2px solid var(--md-accent-fg-color);
  outline-offset: 3px;
  border-radius: 0.2rem;
}

.md-typeset .cividoc-category-list li > a strong,
.md-typeset .cividoc-audience-list li > a strong {
  font-weight: 650;
}

.md-typeset .cividoc-category-meta {
  display: block;
  color: var(--md-default-fg-color--light);
  font-size: 0.72rem;
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: 0.015em;
}

.md-typeset .cividoc-category-summary {
  display: block;
  color: var(--md-default-fg-color--light);
  font-size: 0.78rem;
  line-height: 1.55;
}

.md-typeset .cividoc-category-details {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem 0.7rem;
  margin-top: auto;
  padding-top: 0.45rem;
  color: var(--md-default-fg-color--lighter);
  font-size: 0.68rem;
  line-height: 1.4;
}

.md-typeset .cividoc-category-details span {
  display: inline-flex;
  align-items: center;
}

.md-typeset
.cividoc-category-details
span + span::before {
  margin-right: 0.7rem;
  content: "·";
}

@media screen and (max-width: 44rem) {
  .md-typeset .cividoc-category-list ul,
  .md-typeset .cividoc-audience-list ul {
    grid-template-columns: 1fr;
  }

  .md-typeset .cividoc-category-list li,
  .md-typeset .cividoc-audience-list li {
    padding: 0.9rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .md-typeset .cividoc-category-list li,
  .md-typeset .cividoc-audience-list li {
    transition: none;
  }

  .md-typeset .cividoc-category-list li:hover,
  .md-typeset .cividoc-audience-list li:hover {
    transform: none;
  }
}
"""