

from app.website.views.engine_router import Router, Route
from app.website.views.web import *

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
        warningsFormView,
        ["GET", "POST"]
    )
)

router.add(
    Route(
        "/warning/image/<int:photo_id>",
        messageWarningImageView,
        ["GET", "POST"]
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

router.add(
    Route(
        "/warning/delete/<_id>",
        deleteWarningView,
        ["GET"]
    )
)
router.add(
    Route(
        "/warning/delete",
        deleteWarningView,
        [
            "POST"
        ]
    )
)


router.add(Route(
    "/clients",
    showClients,
    [
        "GET"
    ]
))

router.add(Route(
    "/clients/<int:client_id>",
    showClients,
    [
        "GET"
    ]
))

router.add(
    Route(
        "/message/create/<int:follow_id>",
        messageRegister,
        [
            "POST"
        ]
    )
)
