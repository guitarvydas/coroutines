let continuations = [];

function A () {
    const self = {
        A1: function () {
            console.log ("A 1");
            return (self.A2);
        },
         A2: function () {
             console.log ("A  2");
             return (self.A1);
        }
    };
    return self.A1;
    return;
}

function B () {
    const self = {
        B1: function () {
            console.log ("B 1");
            return self.B2;
        },
         B2: function () {
            console.log ("B  2");
            return self.B1;
        }
    };
    return self.B1;
}

function dispatcher () {
    continuations.push (A());
    continuations.push (B());
    let i = 10;
    let f;
    while (i > 0) {
	// circular queue - pull ready continuation from front of queue
        f = continuations.shift ();
	// resume continuation, when it yields, it returns the next continuation
        let cont = f();
	// push resulting next continuation onto back of queue
	continuations.push (cont);
        i -= 1;
    }
}

dispatcher ();
