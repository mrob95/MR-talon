tag: user.terminal
and tag: user.kubectl
-
cube [control]: "kubectl "

cube create: "kubectl create "
cube expose: "kubectl expose "
cube run: "kubectl run "
cube set: "kubectl set "
cube run container: "kubectl run-container "

cube explain: "kubectl explain "
cube get: "kubectl get "
cube edit: "kubectl edit "
cube delete: "kubectl delete "

cube rollout: "kubectl rollout "
cube rolling update: "kubectl rolling-update "
cube scale: "kubectl scale "
cube auto scale: "kubectl autoscale "

cube certificate: "kubectl certificate "
cube top: "kubectl top "
cube drain: "kubectl drain "
cube taint: "kubectl taint "
cube (cord | cordon): "kubectl cordon "
cube (uncord | uncordon): "kubectl uncordon "
cube cluster (info | information): "kubectl cluster-info "

cube describe: "kubectl describe "
cube logs: "kubectl logs "
cube attach: "kubectl attach "
cube exec: "kubectl exec "
cube port forward: "kubectl port-forward "
cube proxy: "kubectl proxy "
cube copy: "kubectl cp "
cube auth: "kubectl auth "

cube diff: "kubectl diff "
cube apply: "kubectl apply "
cube patch: "kubectl patch "
cube replace: "kubectl replace "
cube wait: "kubectl wait "
cube convert: "kubectl convert "
cube customize: "kubectl kustomize "

cube label: "kubectl label "
cube annotate: "kubectl annotate "
cube completion: "kubectl completion "

cube (interface | API): "kubectl api "
cube interface resources: "kubectl api-resources "
cube interface versions: "kubectl api-versions "
cube config: "kubectl config "
cube help: "kubectl help "
cube plugin: "kubectl plugin "
cube version: "kubectl version "

cube [rollout] restart [deployment]: "kubectl rollout restart deployment "

cube search {user.kubectl_object} [<phrase>]:
    insert("kubectl get {kubectl_object} | egrep {phrase}")

cube {user.kubectl_action} [{user.kubectl_object}]:
    insert("kubectl {kubectl_action} ")
    insert(kubectl_object or "")
    insert(" ")

cube detach:
    key("ctrl-p")
    key("ctrl-q")
cube shell: user.insert_between("kubectl exec -it ", " -- /bin/bash")

# skaffold
scaffold run: "skaffold run "
scaffold run tail: "skaffold run --tail "
scaffold dev: "skaffold dev "
scaffold debug: "skaffold debug "
scaffold build: "skaffold build "
scaffold test: "skaffold test "
scaffold deploy: "skaffold deploy "
scaffold delete: "skaffold delete "
scaffold render: "skaffold render "
scaffold apply: "skaffold apply "
scaffold verify: "skaffold verify "
scaffold init: "skaffold init "
scaffold completion: "skaffold completion "
scaffold config: "skaffold config "
scaffold diagnose: "skaffold diagnose "
scaffold fix: "skaffold fix "
scaffold schema: "skaffold schema "
scaffold survey: "skaffold survey "
scaffold version: "skaffold version "

jason path:
    " -o jsonpath={{.data.}}"
    key(left)
