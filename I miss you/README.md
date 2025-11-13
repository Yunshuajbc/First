# 小陈生日快乐 - 网页版浪漫弹窗

这是一个可爱的生日祝福网页，点击"确认"按钮后会出现多个彩色弹窗，显示温馨的祝福消息。

## 📁 文件说明

- `index.html` - 主页面文件（可直接在浏览器打开）
- `love_popup.py` - Python 桌面版弹窗程序（原版）

## 🌐 部署方法

### 方法一：本地测试

直接双击 `index.html` 文件，即可在浏览器中打开并测试。

### 方法二：免费静态网站托管（推荐）

#### 选项 1：GitHub Pages（完全免费）

1. 在 GitHub 创建新仓库
2. 上传 `index.html` 文件
3. 在仓库设置中启用 GitHub Pages
4. 访问链接：`https://你的用户名.github.io/仓库名/`

#### 选项 2：Vercel（推荐，最简单）

1. 访问 https://vercel.com
2. 注册账号（可用 GitHub 账号登录）
3. 点击 "New Project"
4. 上传包含 `index.html` 的文件夹
5. 几秒钟后自动生成链接

#### 选项 3：Netlify

1. 访问 https://netlify.com
2. 注册账号
3. 拖拽文件夹上传
4. 自动生成链接

#### 选项 4：中国国内服务

- **Gitee Pages**（码云）
- **云开发 CloudBase**（腾讯云）
- **静态网站托管**（阿里云/腾讯云）

### 方法三：自定义域名（可选）

如果购买了域名，可以：

- 配置 DNS 指向托管服务
- 使用子域名，如：`xiaochenhappybirthday.yourdomain.com`

## 🔗 关于中文 URL

### URL 编码方式

URL 中不能直接使用中文，会被自动编码：

- `小陈生日快乐` → `%E5%B0%8F%E9%99%88%E7%94%9F%E6%97%A5%E5%BF%AB%E4%B9%90`

### 推荐方案

#### 1. 使用 URL 路径（最简单）

```
https://yourdomain.com/xiaochenhappybirthday
或
https://yourdomain.com/小陈生日快乐  (浏览器会自动编码)
```

#### 2. 使用短链接服务（显示中文）

- **dwz.cn**（短网址）
- **sina.lt**（新浪短链接）
- 可以设置自定义短链接，如：`dwz.cn/xiaochenhappybirthday`

#### 3. 使用子域名

```
https://xiaochenhappybirthday.yourdomain.com
```

## 📱 微信中打开

在微信中发送链接后，点击链接会在微信内置浏览器中打开。页面已做移动端适配，在微信中显示正常。

## ✨ 功能特点

- 💌 精美的生日邮件风格界面
- 🎈 点击"确认"按钮触发弹窗
- 🌈 50 个随机彩色弹窗
- 💝 30 条温馨祝福消息
- 📱 完美适配移动端（微信）
- 🎉 流畅的动画效果

## 🛠️ 自定义修改

### 修改弹窗数量

在 `index.html` 中找到：

```javascript
const maxPopups = 50;
```

修改数字即可。

### 修改弹窗间隔

找到：

```javascript
setTimeout(() => createPopupsSequentially(count - 1), 100);
```

修改 100（毫秒）即可。

### 修改弹窗显示时间

找到：

```javascript
setTimeout(() => {
    popup.classList.add('fadeOut');
    ...
}, 5000);
```

修改 5000（毫秒，即 5 秒）即可。

## 📞 技术支持

如有问题，请检查：

1. 浏览器是否支持现代 JavaScript
2. 是否在 HTTPS 环境下（某些浏览器要求）
3. 移动端显示是否正常

---

**祝你使用愉快！🎂🎉**
