let bookmark = {"A": null, "B": null};
let next = "A";

function A () {
    const self = {
        idle: function () {
            console.log ("A 1");
            bookmark.A = self.running;
            next = "B";
            return;
        },
         running: function () {
            console.log ("A  2");
            bookmark.A = self.idle;
            next = "B";
            return;
        }
    };
    bookmark.A = self.idle;
    return;
}

function B () {
    const self = {
        idle: function () {
            console.log ("B 1");
            bookmark.B = self.running;
            next = "A";
            return;
        },
         running: function () {
            console.log ("B  2");
            bookmark.B = self.idle;
            next = "A";
            return;
        }
    };
    bookmark.B = self.idle;
    return;
}

function coroutine_manager () {
    A();
    B();
    let i = 10;
    let f;
    while (i > 0) {
        f = bookmark[next];
        f();
        i -= 1;
    }
}

coroutine_manager();
