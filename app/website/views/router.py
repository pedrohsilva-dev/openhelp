from app.website.views.web import *
from app.website.views.engine_router import Router, Route

router = Router()

router.add(
    Route(
        "/home",
        homeView,
        ["GET"]
    )
)

router.add(
    Route(
        "/login",
        loginView,
        ["GET", "POST"]
    )
)

router.add(
    Route(
        "/logout",
        logoutView,
        ["GET"]
    )
)

router.add(
    Route(
        "/register",
        registerView,
        ["GET", "POST"]
    )
)

router.add(
    Route(
        "/messages/<int:company>/<int:client>",
        messageOuve,
        ["GET", "POST"]
    )
)

router.add(
    Route(
        "/messages",
        messagesView,
        ["GET"]
    )
)

router.add(
    Route(
        "/warnings",
        warningsView,
        ["GET"]
    )
)
router.add(
    Route(
        "/warnings/form",
        homeView,
        ["GET", "POST"]
    )
)

router.add(
    Route(
        "/warning/image/<int:photo_id>",
        messageWarningImageView,
        ["GET"]
    )
)
router.add(
    Route(
        "/client/image/<int:photo_id>",
        messageClientImageView,
        ["GET"]
    )
)
router.add(
    Route(
        "/company/profile",
        companyImageView,
        ["GET"]
    )
)

router.add(
    Route(
        "/index",
        index,
        [
            "GET", "POST"
        ]
    )
)


router.add(
    Route(
        "/profile",
        profile,
        [
            "GET", "POST"
        ]
    )
)


router.add(
    Route(
        "/update",
        updateView,
        [
            "GET", "POST"
        ]
    )
)

router.add(
    Route(
        "/delete",
        deleteView,
        [
            "GET", "POST"
        ]
    )
)
