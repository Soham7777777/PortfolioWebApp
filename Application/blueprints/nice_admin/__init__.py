from flask import Blueprint, render_template, url_for
from .ui_components import NavDrodownItemComponent, NavDropdownComponent, NavHeadingComponent, NavItemComponent

bp = Blueprint('NiceAdmin', __name__, url_prefix='/nice-admin', static_folder='static', template_folder='templates')

@bp.get('/')
def home():
    dashboard = NavItemComponent(url=url_for('NiceAdmin.dashboard'), icon_name='grid', name='Dashboard', selected=True)
    tables = NavDropdownComponent(icon_name='layout-text-window-reverse', name='Tables',
    items=[
        NavDrodownItemComponent(url=url_for('NiceAdmin.sample_table'), name='table1'),
        NavDrodownItemComponent(url=url_for('NiceAdmin.sample_table'), name='table2'),
        NavDrodownItemComponent(url=url_for('NiceAdmin.sample_table'), name='table3'),
        NavDrodownItemComponent(url=url_for('NiceAdmin.sample_table'), name='table4')
    ]
    )
    return render_template('nice_admin/index.html', dashboard=dashboard, tables=tables)

@bp.get('/dashboard')
def dashboard():
    return render_template('nice_admin/main/dashboard.html'), {"HX-Trigger-After-Settle": "DashboardLoaded"}

@bp.get('/sample_table')
def sample_table():
    return render_template('nice_admin/main/table.html')