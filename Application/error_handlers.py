from werkzeug import exceptions
from werkzeug.http import HTTP_STATUS_CODES
from typing import cast
from flask import redirect, url_for
from Application.ui_components import OOBComponent, ToastComponent
import json

def toastify_default_errors(e: exceptions.HTTPException):
        code: int
        description: str | list
        
        if issubclass(type(e), exceptions.InternalServerError):
            UnhandledException = cast(exceptions.InternalServerError, e)
            if UnhandledException.original_exception is not None and any(args:=UnhandledException.original_exception.args):
                description = args[0] if len(args)==1 else list(args)
            else:
                description = UnhandledException.description
            
            code = UnhandledException.code
        else:
            description = e.description # type: ignore
            code = e.code # type: ignore
        
        toast = ToastComponent(
            header=HTTP_STATUS_CODES[code],
            header_text_color='warning',
            icon_name='patch-exclamation-fill',
            body=description if type(description) == str else ', '.join(description)
        )
        oob = OOBComponent(
            element_id='toaster',
            tag='div',
            hx_swap_oob='innerHTML',
            content=toast.render()
        )

        return oob.render(), 422, {"HX-Reswap": "none", "HX-Trigger-After-Settle": json.dumps(dict(Toastify=toast.element_id))}

def handle_notfound_errors(e: exceptions.NotFound):
    return redirect(url_for('home'))