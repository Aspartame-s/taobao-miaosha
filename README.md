# taobao_miaosha

学习使用python中的selenium，通过webdriver.Chrome实现模拟访问页面并点击操作

本代码功能：
  打开淘宝界面，实现扫码登陆或者账户名+密码（拖拉验证框待解决）登陆
  为了更快速的抢到商品，根据淘宝的机制简化了部分操作，所以需要一部分手动操作

  1.首先将需要抢购的商品加入购物车
  2.运行代码后，手动在页面打开购物车，并勾选需要抢购的商品（运行代码后会自动打开淘宝登陆页面）
  3.点击结算按钮，跳转到提交订单页面


`吐槽！！`
`我看了github很多代码，以及网络上的视频，很多人的代码都是登陆之后，自动点击购物车，自动勾选，自动结算，自动提交订单，我个人觉得点击购物车和勾选商品不太需要自动化，所以没做，这样也方便自己勾选`

`最重要的一点就是结算以及提交订单这两步操作，现在的很多自动抢购的代码都会停留在结算页面，然后等时间到了之后，先自动点击结算按钮，然后会跳转到提交订单页面，再自动点击提交订单按钮，等你这两步操作下来都过去一秒多了，还没我自己抢的快`

`不知道是不是原来的淘宝不让提前点击结算，因为从点击完结算到跳转到提交订单页面的过程，中间是有页面跳转的，这个时间浪费的太多了，因为只有点击提交订单按钮，淘宝才会认为你锁单了，现在的淘宝可以提前点击结算，直接进入到提交订单页面，所以我这次的代码就是在达到预设时间后，点击提交订单按钮`

`另外，还优化了锁定 提交订单 按钮的逻辑，在达到预设时间前20秒，我会提前锁定到提交按钮，这样就不用在预设时间到的时候再去找按钮，经本人测试，这样时间能提前个0.06秒，看着不多，但本来就是跟时间赛跑的游戏，能提前一点就能增加一点胜率`

注意：要修改的地方一处是抢购时间
另外需要下载对应自己chrome浏览器的chromedriver

如果对您有用，麻烦给个star，谢谢

有问题可以微信 c327127960 免费解答
