# cctv-footage-memory-reducer

<a href="https://github.com/manoj633/cctv-footage-memory-reducer/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/manoj633/cctv-footage-memory-reducer?style=for-the-badge"></a>
![Repository Size](https://img.shields.io/github/repo-size/manoj633/cctv-footage-memory-reducer?style=for-the-badge)
![Lines of Codes](https://img.shields.io/tokei/lines/github.com/manoj633/cctv-footage-memory-reducer?style=for-the-badge)

![GitHub last commit](https://img.shields.io/github/last-commit/manoj633/cctv-footage-memory-reducer?style=for-the-badge)

---

👋 Hi <br>
I am Manoj M .This project is a simple application that stores camera captured footage only on motion detection

```
📦 cctv footage memory reducer
├─ .gitignore
├─ LICENSE
├─ README.md
└─ application.py
```

### Technology/Tools used

- Python 3
- OpenCV
- numpy

---

## Algorithm used

### MOG2 (Mixture of Gaussian)

In this method, a mixture of k Gaussians distributions models each background pixel, with values for k within 3 and 5. It is assumed that different distributions represent each different background and foreground colors. The weight of each one of those used distributions on the model is proportional to the amount of time each color stays on that pixel. Therefore, when the weight of a pixel distribution is low, that pixel is classified as foreground.

### 📝 License

[MIT](https://choosealicense.com/licenses/mit/)

If you like this don't forget to ⭐ the repository.

Thank You for visiting
Have a nice day 😊
