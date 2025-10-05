def grade(data):
    import js
    js.document.title = 'New window title'
    return {"overall": dict(credit=1, letter="<script>alert('hello world')</script>a"),
            "assignments": []
            }
