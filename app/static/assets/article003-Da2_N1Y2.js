const g="data:text/markdown;base64,IyBQcm9taXNzYSBkZXVzIGFjY2VwdGlvcg0KDQojIyBNYWxvIHF1aWQgbWVkaXVtIGV0IGhhYmVyZXQgbWVvIHNvbHVzDQoNCkxvcmVtIG1hcmtkb3dudW0gZmx1bWluaXMgY29udHJhLCBzaW1pbGxpbXVzIFtidXN0YQ0KYXVyb10oaHR0cDovL3d3dy5yYWRpY2VzdHVyYXF1ZS5uZXQvKSBjYXBlcmUgc2FlcGUgKm1vcmllbnMgbWUgbWloaSouIFJlZGRpdCB2ZXINCnBvcHVsdXMgaW4gKippcHNlIGZpbmVzKio/DQoNCiAgICB2YXIgb2xlX2RldmVsb3BtZW50X2lwdiA9IGRlc2t0b3Bfbm9jKDUzICogaG90LCBzY3JvbGxpbmdVc2IsDQogICAgICAgICAgICB3aW5zQ2Fycmllckpzb24uY3Jvc3NwbGF0Zm9ybSg1LCBwYXJpdHlBaWZmLCBkZHJSZWNvcmREcml2ZSkpIC0NCiAgICAgICAgICAgIGdpZ2FieXRlTGlua0RyaXZlIC0gdWRwSW50ZWdyYXRlZE92ZXJ3cml0ZShyZXN0b3JlT3V0Ym94UG9ydCwNCiAgICAgICAgICAgIGZ1bmN0aW9uX3RleHRfYmFyLCBzb2Z0X3N0YXRpb25fY2hpcHNldCk7DQogICAgdmFyIG9wdGljYWxfb3B0aWNhbF9kb25hdGlvbndhcmUgPSBydW50aW1lLnZpZXdfc3NoKGJhY2tsaW5rRGF0YUJvdW5jZSArDQogICAgICAgICAgICBidXNKc2YsIGNlbGxUZXh0Q21zICsgdm9sdW1lTWV0YUFkc2wpICsgcHJvbXB0X21vdW50X2Jvb3QoDQogICAgICAgICAgICB3YW1wX3NlcnZlcl9lICogbWF4aW1pemVDbW9zLCA5OSk7DQogICAgdmFyIHZmYXRfbGlzdHNlcnYgPSBjZXJ0aWZpY2F0ZVdpZGdldDsNCiAgICB2YXIgZmlvcyA9IHVzZXJfcmVndWxhcihtYWNfZHJpdmUgKyBob3N0RXhwcmVzc1RlYmlieXRlKTsNCiAgICBkc2xQYWdlKGFkZHJlc3NLZXlib2FyZElibShiYWNrdXBHaWZMYW5ndWFnZSArIGdhdGV3YXkpLCB1cmwsDQogICAgICAgICAgICBkb21haW5DbGlwYm9hcmRXb3JtKGNoaXBfZ3BzX21ldGFkYXRhKSArIG5vc3FsKTsNCg0KIyMgRXQgbWVkaW8gZ3JlZ2lidXMgcmVsaW5xdWFtIGFzdHUgYWVxdWFudHVyIG5hdHVzDQoNCklyZSB1dCBkZXh0cmEgZXNzZSwgbWFudXMgZXhzcGF0aWFudHVyIGZpYnJpczsgZXJpdCBhdHRvbGxlcmUgbHVtaW5hIHNpLCBoYXN0YQ0KcXVvdCBbbGV2ZSBpbnNpYmlsYXRdKGh0dHA6Ly9tb2RvLWlwc2EubmV0L2V0LWF0cXVlLmh0bWwpLiBVdCBpdWJlYXMgcmVuYXJybw0KcXVpbiBkaWdudW0sIGlsbGUgdW1vcmUsIHBhY2FsaWJ1cyBzaW5pc3RyYSwgbnVkYW5zIG1hbnUgaXV2ZW5pcyBwYXNzdQ0Kc3BvbGlvcXVlLCB2dWx0dXNxdWUuIENhZWx1bXF1ZSBwcm9waW9yYXF1ZSB0aGFsYW1pLCBxdWFtcXVhbSBhcmN1cyBtb3JpZW5zLA0KY29uYXRhIGRpeGkgY2FlbG9xdWUuDQoNCiMjIFR1cmJhdGlzIG5hdGFsaXMgdGFuZ2kgc2VkIGVzdA0KDQpGZXJ1bnR1ciAqc2Vuc3VzKiB2dWxuZXJlIGRlZHVjdGFzLCBbZWdyZXNzYSB2aWxsaXNxdWVdKGh0dHA6Ly9pbnJpdGEuY29tL2EpDQpwYXVsdW0gc2VjdXJ1cyBxdW9uZGFtIHNhZXBlIGRlbnN1bXF1ZSBpbnZpdGEsIHN1YnNpZGVyZSBpbmR1cnVpdCBzaWMgZXRzaS4NClF1b3F1ZSBpbiBvc2N1bGEgW2hhYml0YW5kYWVdKGh0dHA6Ly9zYXRpYWltaXRhdG9yLm9yZy9hZGR1bnQtY3VtLnBocCkgY29ybnVhDQpmdXJpYnVuZGEgZnVnYXRhcyBnZW5pcywgdGVycmFzIHByb2ZlY3R1cmEsIG5lYnVsYXMgYSBxdW9uaWFtIGZ1bHZpcyBhZHNwaWNpdA0KbWF0dXJ1cy4gQWVzdHVzICoqdGFudGlzIGN1bmN0b3MgVGhlc3BpYWRlcyoqIE5lbGVpdXMgKipwb250dW0qKi4gUXVvcXVlIHVuZGlzLA0KZGlmZnVkZXJlIG55bXBoYSB0b2xsZW5zLg0KDQojIyBUcmlidXMgcmVnaXMNCg0KRW5pbSB1bHRpbWEgb3Jhdml0LCB2aXNhIGFydmEgRWNoaW9uaW8gUGV1Y2V0aW9zcXVlIHZlbmkgcGF0dWxhIGhvcnRhdG9yIHF1b3F1ZSwNCm1vcmEgdmluY2UuIEZ1ZXJhbnQgaHVjIFtodW11bV0oaHR0cDovL3B1Z25hLmlvL29ic2Vzc2EtcHVsY2hlcnJpbXVzKTogdGVuYXgNCnBldGl0IHNhbmFlIGNhdGVuYXMgYmlzIFByb2NuZXM7IGEuDQoNCiAgICBpZiAoYmFuaykgew0KICAgICAgICBzb3VuZERlZnJhZ21lbnRTY2FuID0gZGF0YTsNCiAgICAgICAgYXJwQmluU29jaWFsLmNvbXB1dGluZ19hZGZfbXVsdGl0aHJlYWRpbmcgKz0gcHVtICogY2xlYW4gKyAzNDsNCiAgICB9IGVsc2Ugew0KICAgICAgICBzbGkgPSAxNjgzMDcgKiBjeWJlcmJ1bGx5aW5nX3Nwb29maW5nICsgd2FtcERvdE1hcmtldC5jYXJkKA0KICAgICAgICAgICAgICAgIHlvdHRhYnl0ZV9wbGF5X21lbnUsIDUsIHNzbCk7DQogICAgfQ0KICAgIGRpbW1JbnRlbGxpZ2VuY2UubG9naWNfc291cmNlX3plcm8gKz0gLTQ7DQogICAgZXhwcmVzc19wcmltYXJ5LnBpdGNoICs9IHdlYm1hc3RlcjsNCiAgICB2YXIgcHVtID0gaWJtSW50ZWdyYXRlZDsNCiAgICB2YXIgdXNlcl9zaXRlX3ByaW50ZXIgPSB3YW1wVnJtbER1cGxleCArIGJvdF9jbG9iX3JlYWQ7DQoNCiMjIEV0IGFldGFzIG11bmVyZSBsaXF1aWRhcnVtIHZ1bHRpYnVzIHBlcmN1c3NhbXF1ZSBub24NCg0KTW92aXQgKiplc3QqKiBkZWllY3RvIGZhbWEgUGFuYXF1ZSBpbnBydWRlbnMgdXQgZGljYW0gbmVjIGVzdCBxdWFydW0gbWFudXMgVGhlbWkNCk5pb2JlIHByaW11bSBkZXByZW5kaW11ci4gUHJhZWNpcHVlIFBhbGxhZGlzIGluc2FubyBtYW51cyBxdWksIGZlcmEgY2FwaWxsaXMNCnBhcnRpbSB2ZW50b3J1bXF1ZSBwZWRlcyBpdW5jdGlzLCBkaXV0dXJuaW9yIHNpIG5vdmllbnMgY2F1ZGFtLg0KDQpOYXRvcnVtIHZlcnRpdCBwdWVyIGFzdHUgKnZpZ29yIGRpbGFwc2EgcXVvcXVlKiBMZWxleCBlc3Qgc29yb3J1bSB0YWVkYQ0Kc2VuaW9yaWJ1cyBzdGlycGVtIGNvbmZlc3NhcXVlLiBTcXVhbW9zb3MgQWNvZXRlIGxldGlmZXJpcyBlc3QgYWV0YXMgbWlzZXJlcmUgZXQNCmZlY2l0LCBub24gaW50ZXJkdW0uIFJldHJvIGRvbWVzdGljdXMgYW5uaXMsIHZpcmdhLCBpbiBhcnR1cywgW21vdGEgaXBzbw0KdmVyYmFdKGh0dHA6Ly9hbGNtZW5lLXF1ZXJlbGxhcy5jb20vKSBydXJzdXMgZnJheGluZWFtIG1vbGlidXMgdHJhY3R1PyBbQXN0eWFuYXgNCmFiaXRdKGh0dHA6Ly9pZ25pYnVzLWV4cGxpY2F0LmlvL2RlZmVuZGVyZSkuIFRhbSBnZW5lciBjYXBpZW5kYSBvYmxpcXV1bSBpbnF1ZS4NCg==";export{g as default};
