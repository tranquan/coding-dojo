/**
 * Learning about Iterator and Generator
 */

// ---------------------------------------------
// simple iterator
function* makeIterator() {
  for (let i = 0; i < 5; i++) {
    yield i;
  }
}

function test1() {
  const iter = makeIterator();
  console.log(iter.next());
  console.log(iter.next());
  console.log(iter.next());
  console.log(iter.next());
}

// ---------------------------------------------
// Custom iterator
class FibonacciGenerator {
  current = 0;
  next = 1;

  reset() {
    this.current = 0;
    this.next = 1;
  }

  *[Symbol.iterator]() {
    while (true) {
      yield this.current;
      [this.current, this.next] = [this.next, this.current + this.next];
    }
  }
}

function test2() {
  const gen = new FibonacciGenerator();
  const iter = gen[Symbol.iterator]();
  console.log("---generate fibonacci");
  for (let i = 0; i < 3; i++) {
    console.log(iter.next());
  }
  console.log("---reset");
  gen.reset();
  for (let i = 0; i < 3; i++) {
    console.log(iter.next());
  }
}

// ---------------------------------------------
// async with iterator

// the purpose is making timeout work sync
function timeout(callback) {
  setTimeout(() => {
    callback(Math.floor(Math.random() * 100));
  }, 1000);
}

function timeoutWrapper() {
  return function (callback) {
    timeout(callback);
  };
}

// idea is using yield to pause execution in runTask so we can return the value in next() call
function runTask(taskDef) {
  let task = taskDef();
  let result = task.next();

  function step() {
    if (!result.done) {
      if (typeof result.value === "function") {
        result.value(function (data) {
          result = task.next(data);
          step();
        });
      } else {
        result = task.next();
        step();
      }
    }
  }

  step();
}

function test3() {
  console.log("---test3 start");

  // old way
  // timeout((result) => {
  //   console.log("---timeout done! result: ", result);
  // });

  // new way, no need callback
  runTask(function* () {
    console.log("---runTask start");
    const result = yield timeoutWrapper();
    console.log("---runTask done, result: ", result);
  });

  console.log("---test3 end");
}

// ---------------------------------------------
// Main
// test1();
// test2();
test3();
