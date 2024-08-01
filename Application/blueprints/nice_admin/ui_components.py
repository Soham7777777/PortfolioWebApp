from Application.ui_components import BaseComponent
from dataclasses import dataclass, field

@dataclass
class NavItemComponent(BaseComponent):
    template_path: str = field(init=False, default='nice_admin/macros/nav_item.html')
    macroname: str = field(init=False, default='NavItemMacro')

    url: str
    icon_name: str
    name: str
    selected: bool = False

@dataclass
class NavHeadingComponent(BaseComponent):
    template_path: str = field(init=False, default='nice_admin/macros/nav_heading.html')
    macroname: str = field(init=False, default='NavHeadingMacro')

    heading: str

@dataclass
class NavDrodownItemComponent(BaseComponent):
    template_path: str = field(init=False, default='nice_admin/macros/nav_dropdown_item.html')
    macroname: str = field(init=False, default='NavDropdownItemMacro')

    url: str
    name: str
    selected: bool = False

@dataclass
class NavDropdownComponent(BaseComponent):
    template_path: str = field(init=False, default='nice_admin/macros/nav_dropdown.html')
    macroname: str = field(init=False, default='NavDropdownMacro')

    icon_name: str
    name: str
    items: list[NavDrodownItemComponent]
